# ----------------------------------------------------------
# Storage Port
# ----------------------------------------------------------
import asyncio
import os
import pickle
import re
import time
import sys
import traceback
from typing import List
from multiprocessing import Process
import random
from operator import le, lt, ge, gt, eq
import yaml
from logging import ERROR, getLogger
from enum import Enum, IntEnum  # for DatalakeBehavior?

# import hashlib
# import uuid

# from surrealdb import Surreal
from surrealist import Surreal as Surrealist


from agptools.logs import logger
from agptools.helpers import parse_uri, build_uri, DATE
from agptools.containers import merge as merge_dict, build_dict

from syncmodels.definitions import (
    REVERSE_SORT_KEY,
    WAVE_RESUMING_INFO_KEY,
)
from syncmodels.http import (
    # guess_content_type,
    # ALL_JSON,
    CONTENT_TYPE,
    # USER_AGENT,
    APPLICATION_JSON,
)

from .helpers.importers import JSONVerter

# from surrealist.connections.connection import logger as surreal_logger
# from .exceptions import BadData
from .definitions import (
    DIRECTION_KEY,
    DIRECTION_DESC,
    filter_4_compare,
    GRACE_PERIOD_KEY,
    ID_KEY,
    JSON,
    MONOTONIC_KEY,
    monotonic_wave,
    MONOTONIC_SINCE_KEY,
    MONOTONIC_SINCE_OPERATOR,
    MONOTONIC_SINCE_VALUE,
    ORDER_KEY,
    ORG_KEY,
    QUERY,
    REG_SPLIT_PATH,
    WAVE_INFO_KEY,
    PARAMS_KEY,
    KIND_KEY,
    PREFIX_URL,
    URI,
    WHERE_KEY,
    SORT_KEY,
    LIMIT_KEY,
    WAVE_LAST_KEY,
)
from .crud import (
    DEFAULT_DATABASE,
    DEFAULT_NAMESPACE,
    parse_duri,
    tf,
    iStorage,
    iPolicy,
    iConnection,
    iConnectionPool,
)
from .requests import iResponse

from .wave import (
    iWaves,
    TUBE_DB,
    TUBE_META,
    TUBE_NS,
    TUBE_SYNC,
    TUBE_WAVE,
    TUBE_SNAPSHOT,
    TUBE_TABLES,
)
from .helpers import expandpath
from .helpers.crawler import SortKeyFinder


# ---------------------------------------------------------
# Loggers
# ---------------------------------------------------------


# from 0.5.2 surrealist uses root default level
for _ in (
    "surrealist.connection",
    "surrealist.connections.websocket",
    "websocket_connection",
):
    getLogger(_).setLevel(ERROR + 1)


log = logger(__name__)
log_records = logger(f"{__name__}.records")


# REGEXP_FQUI = re.compile(r"((?P<ns>[^/]*?)/)?(?P<table>[^:]+):(?P<uid>.*)$")
def split_fqui(fqid):
    "try to split FQUID into table and uid"
    try:
        table, uid = fqid.split(":")
        return table, uid
    except ValueError:
        return fqid, None


# ---------------------------------------------------------
# Data Store / Ignore Policies
# ---------------------------------------------------------


class DataInsertionPolicy(iPolicy):
    "when a record must be inserted or not"
    # TODO: REVIEW, this code will not work with current version

    async def action(self, mode, thing, data):
        if mode in (iWaves.MODE_SNAPSHOT,):
            return self.STORE

        if mode in (iWaves.MODE_TUBE,):
            # check if last data is the same but MONOTONIC_KEY
            tube_name = thing.split(":")[0]
            fquid = f"{TUBE_WAVE}:{tube_name}"

            # TODO: use sync or cache for faster execution
            last = await self.storage.last_wave(fquid)
            _last = filter_4_compare(last)
            _data = filter_4_compare(data)
            if _last == _data:
                return self.DISCARD

            return self.STORE

        return self.DISCARD


# ---------------------------------------------------------
# Main Storage interface proposal
# ---------------------------------------------------------


class Storage(iStorage):
    def __init__(self, url, policy=DataInsertionPolicy):
        super().__init__(url=url, policy=policy)
        self.background = []

    def running(self):
        self.background = [p for p in self.background if p.is_alive()]
        return len(self.background)

    async def info(self):
        raise NotImplementedError()

    async def since(self, fqid, wave, max_results=100):
        "return the last objects since a wave"
        raise NotImplementedError()


# ---------------------------------------------------------
# Main Storage interface proposal
# ---------------------------------------------------------


# ---------------------------------------------------------
# Storages Ports used by hexagonal architecture
# TODO: review if storage may replace them all
# ---------------------------------------------------------


class StoragePortConnectionPool(iConnectionPool):
    def __init__(self, url, storage: Storage):
        super().__init__(url)
        self.storage = storage

    async def _connect(self, *key) -> iConnection:
        url = parse_uri(self.url)
        # url["fscheme"] = "http"
        # url["path"] = ""
        url = build_uri(**url)

        connection = iMemConnection(storage=self.storage)

        self.connections[key] = connection
        namespace, database = key
        connection.use(namespace, database)
        # setattr(connection, "database", database)
        # create initial database layout
        # await self._update_database_layout(connection)
        self.last_connection = connection
        return connection


class StoragePort(Storage):
    PATH_TEMPLATE = "{fscheme}/{xhost}/{_path}"

    def __init__(self, url="./db"):
        super().__init__(url=url)
        url = expandpath(url)
        if not os.path.exists(url):
            os.makedirs(url, exist_ok=True)
        self.url = url
        self.cache = {}
        self._dirty = {}
        self.connection_pool = StoragePortConnectionPool(url, storage=self)

    def _file(self, uri: URI):
        _uri = parse_duri(uri)
        path = self.PATH_TEMPLATE.format_map(_uri)
        path = f"{self.url}/{path}"
        path = os.path.abspath(path)
        return path

    def load(self, uri: URI, force=False):
        _uri = parse_duri(uri)
        simplified = "{fscheme}://{xhost}/{_path}".format_map(_uri)

        universe = self.cache.get(simplified)
        if force or universe is None:
            path = self._file(simplified)
            if os.path.exists(path):
                try:
                    universe = self._real_load(path)
                except Exception as why:  # pragma: nocover
                    log.warning(why)  # pragma: nocover
            if universe is None:
                universe = {}
            self.cache[simplified] = universe
        return universe

    _load = load

    def _save(self, pattern: URI, pause=0, force=False):
        for uri in list(self._dirty):
            if re.match(pattern, uri):
                if self._dirty.pop(uri, None) or force:
                    universe = self.load(uri)
                    path = self._file(uri)
                    self._real_save(path, universe, pause=pause)

    def _real_load(self, path):
        raise NotImplementedError()

    def _real_save(self, path, universe, pause=0):
        raise NotImplementedError()

    async def get(self, uri, query=None, **params):
        _uri = parse_duri(uri)
        # uri = build_uri(**_uri)
        universe = self.load(uri)
        if query:
            raise NotImplementedError

        uid = _uri["id"]
        data = universe.get(uid, {})
        return data

    async def set(self, uri: URI, data, merge=False):
        _uri = parse_duri(uri)
        simplified = "{fscheme}://{xhost}/{_path}".format_map(_uri)

        table, uid = split_fqui(uri)
        universe = self.load(simplified)
        if merge:
            data0 = await self.get(uri)
            # data = {** data0, ** data} # TODO: is faster?
            data0.update(data)
            data = data0

        universe[uri] = data
        self._dirty[simplified] = True
        return True

    async def save(self, pattern: URI = None, nice=False, wait=False):
        i = 0
        pattern = pattern or ".*"
        for simplified, table in self.cache.items():
            if re.match(pattern, simplified):
                pause = 1.0 * i if nice else 0
                self._save(simplified, pause=pause)
                i += 1

        # table = table or list(self.cache)
        # if not isinstance(table, list):
        #     table = [table]
        # for i, tab in enumerate(table):
        #     pause = 1.0 * i if nice else 0
        #     self._save(tab, pause=pause)

        log.info("waiting data to be saved")
        while wait and self.running() > 0:
            await asyncio.sleep(0.1)
        return self.running() == 0

    async def info(self, pattern: URI = ".*"):
        "Returns storage info: *tables*, etc"
        _uri = parse_duri(pattern)
        simplified = "{fscheme}/{xhost}/{_path}".format_map(_uri)

        example = self._file("example/foo/bar")
        ext = os.path.splitext(example)[-1]
        regexp = f"{simplified}.*{ext}$"
        top = "."
        for root, _, files in os.walk(top):
            for file in files:
                path = os.path.join(root, file)
                m = re.search(regexp, path)
                if m:
                    # relpath = os.path.relpath(path, self.url)
                    # name = os.path.splitext(relpath)[0]
                    name = path.split(simplified)[-1].split(ext)[0]
                    yield name


class PickleStorage(StoragePort):
    PATH_TEMPLATE = "{fscheme}/{xhost}/{_path}.pickle"

    def _real_load(self, path):
        try:
            universe = pickle.load(open(path, "rb"))
        except Exception as why:  # pragma: nocover
            log.error("%s: Error loading: %s: %s", self, path, why)
            universe = {}
        return universe

    def _real_save(self, path, universe, pause=0):
        try:
            log.debug("[%s] saving: %s", self.__class__.__name__, path)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            pickle.dump(universe, open(path, "wb"))
        except Exception as why:  # pragma: nocover
            log.error("%s: Error savig: %s: %s", self, path, why)


def ulid():
    return str(monotonic_wave())


OPERATORS = {
    ">": gt,
    ">=": ge,
    "<": lt,
    "<=": le,
    "=": eq,
    "==": eq,
}


class iMemConnection(iConnection):
    "Memory cache iConnection implementation"

    HEADERS = {
        CONTENT_TYPE: APPLICATION_JSON,
    }

    def __init__(
        self,
        storage: StoragePort,
        namespace=DEFAULT_NAMESPACE,
        database=DEFAULT_DATABASE,
    ):
        super().__init__()
        self.st = storage
        self.ns = namespace
        self.db = database

    def create(self, thing, data, record_id=None):
        """Helper to store items into StoragePorts that uses cache"""

        if record_id is None:
            record_id = data.get("id") or ulid()

        # data['id'] = record_id  # to mimicking surreal behaviour

        uri = f"{self.ns}://{self.db}/{thing}:{record_id}"
        simplified = f"{self.ns}://{self.db}/{thing}"

        self.st.load(simplified)
        universe = self.st.cache.setdefault(simplified, {})
        universe.setdefault(record_id, {}).update(data)
        self.st._dirty[simplified] = True

        response = iResponse(
            status=200,
            headers={**self.HEADERS},
            links=None,
            real_url=uri,
            body=data,
            result=data,
        )

        return response

    def update(self, thing, data, record_id=None):
        """Hack to store items into StoragePorts that uses cache"""
        return self.create(thing, data, record_id)

    def query(self, thing, data, record_id=None):

        data = dict(data)
        order__ = data.pop(ORDER_KEY, None)
        limit__ = data.pop(LIMIT_KEY, None)
        direction__ = data.pop(DIRECTION_KEY, None)
        since_key__ = data.pop(MONOTONIC_SINCE_KEY, None)
        since_value__ = data.pop(MONOTONIC_SINCE_VALUE, None)
        since_operator__ = data.pop(MONOTONIC_SINCE_OPERATOR, None)
        where__ = data.pop(WHERE_KEY, "")

        simplified = f"{self.ns}://{self.db}/{thing}"
        self.st.load(simplified)
        universe = self.st.cache.setdefault(simplified, {})
        # TODO: create code as reference
        if record_id is None:
            # linear search
            result = []
            for record_id, candidate in universe.items():
                if since_key__ in (MONOTONIC_KEY,):
                    try:
                        wave__ = candidate.get(MONOTONIC_KEY) or int(record_id)
                        op = OPERATORS.get(since_operator__)
                        if not (op and op(wave__, since_value__)):
                            # this candidate doesn't match since_value__
                            continue
                    except Exception as why:  # pragma: nocover
                        # if something fails, we assume candidate won't match
                        continue

                for k, v in data.items():
                    if candidate.get(k) != v:
                        break
                else:
                    candidate = dict(candidate)
                    candidate["id"] = f"{thing}:{record_id}"
                    result.append(candidate)
        else:
            # direct search
            result = [universe.get(record_id)]

        if order__:
            result.sort(key=lambda x: x[order__])

        if direction__:
            if direction__.lower() in ("desc",):
                result.reverse()

        if limit__ is not None:
            result = response[:limit__]
            foo = 1
            # sql += f"\nLIMIT {limit__}"

        response = iResponse(
            status=200,
            headers={**self.HEADERS},
            links=None,
            body=result,
            result=result,
        )

        return response

    def use(self, namespace, database):
        self.ns = namespace
        self.db = database


class YamlStorage(StoragePort):
    PATH_TEMPLATE = "{fscheme}/{xhost}/{_path}.yaml"

    def __init__(self, url="./db"):
        super().__init__(url=url)
        self.lock = 0

    def _real_load(self, path):
        try:
            universe = yaml.load(open(path, encoding="utf-8"), Loader=yaml.Loader)
        except Exception as why:  # pragma: nocover
            log.error("%s: Error loading: %s: %s", self, path, why)
            universe = {}
        return universe

    def _real_save(self, path, universe, pause=0):
        def main(path, universe, pause):
            # name = os.path.basename(path)
            # log.debug(">> ... saving [%s] in %s secs ...", name, pause)
            time.sleep(pause)
            try:
                log.debug("[%s] saving: %s", self.__class__.__name__, path)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                yaml.dump(
                    universe,
                    open(path, "w", encoding="utf-8"),
                    Dumper=yaml.Dumper,
                )
            except Exception as why:  # pragma: nocover
                log.error("%s: Error saving: %s: %s", self, path, why)
            # log.debug("<< ... saving [%s] in %s secs DONE", name, pause)

        if pause > 0:
            # uses a background thread to save in YAML format
            # because is too slow to block the main thread
            # th = threading.Thread(target=main)
            # th.start()
            p = Process(target=main, args=(path, universe, pause), daemon=True)
            self.background.append(p)
            p.start()
            # log.debug("saving daemon is running:  %s", p.is_alive())
            foo = 1
        else:
            main(path, universe, pause=0)


#     async def _connect(self, *key) -> iConnection:
#         url = parse_uri(self.url)
#         # url["fscheme"] = "http"
#         # url["path"] = ""
#         url = build_uri(**url)
#
#         connection = iMemConnection(storage=self)
#
#         self.connections[key] = connection
#         namespace, database = key
#         connection.use(namespace, database)
#         # setattr(connection, "database", database)
#         # create initial database layout
#         # await self._update_database_layout(connection)
#         self.last_connection = connection
#         return connection


class DualStorage(PickleStorage):
    """Storage for debugging and see all data in yaml
    Low performance, but is just for testing
    """

    def __init__(self, url="./db", klass=YamlStorage):
        super().__init__(url=url)
        self.other = klass(url)
        self.background = self.other.background

    async def get(self, uri: URI, query=None, **params):
        _uri = parse_duri(uri)
        simplified = "{fscheme}://{xhost}/{_path}".format_map(_uri)

        other_mtime = None
        if not self.other.lock:
            # table, uid = split_fqui(fqid)
            other_path = self.other._file(simplified)
            mine_path = self._file(simplified)
            if os.access(other_path, os.F_OK):
                other_mtime = os.stat(other_path).st_mtime
            else:
                other_mtime = 0
            if os.access(mine_path, os.F_OK):
                mine_mtime = os.stat(mine_path).st_mtime
            else:
                mine_mtime = 0

        if other_mtime is not None:
            if other_mtime > mine_mtime:
                # replace table from newer to older one
                universe = self.other._load(simplified)
                super()._save(uri, universe, force=True)
                self.cache[simplified] = universe
            data = await super().get(uri, query=None, **params)
        else:
            data = {}
        return data

    def _load(self, uri: URI):
        _uri = parse_duri(uri)
        simplified = "{fscheme}://{xhost}/{_path}".format_map(_uri)

        # table = _uri['_path']
        other_mtime = None
        if not self.other.lock:
            other_path = self.other._file(simplified)  # uri?
            mine_path = self._file(simplified)
            if os.access(other_path, os.F_OK):
                other_mtime = os.stat(other_path).st_mtime
            else:
                other_mtime = 0
            if os.access(mine_path, os.F_OK):
                mine_mtime = os.stat(mine_path).st_mtime
            else:
                mine_mtime = 0

        if other_mtime is not None:
            if other_mtime > mine_mtime:
                # replace table from newer to older one
                universe = self.other._load(uri)
                super()._save(uri, universe, force=True)
                self.cache[simplified] = universe
            data = super()._load(uri)
        else:
            data = {}
        return data

    load = _load

    async def set(self, fqid, data, merge=False):
        """
        other.mtime < mine.mtime
        otherwise user has modifier `yaml` file and `pickle` will be updated
        """
        res1 = await self.other.set(fqid, data, merge)
        res2 = await super().set(fqid, data, merge)
        return all([res1, res2])

    async def put(self, uri: URI, data: JSON = None, **kw) -> bool:
        _uri = parse_duri(uri)
        if _uri.get("id"):
            uri = build_uri(**_uri)
        if data is None:
            data = kw
        else:
            data.update(kw)
        res1 = await super().put(uri, data)
        res2 = await self.other.put(uri, data)
        return all([res1, res2])

    def _save(self, uri, universe=None, pause=0):
        self.other._save(uri, universe, pause=pause)
        super()._save(uri, universe, pause=pause)

    def running(self):
        return super().running() + self.other.running()


# ---------------------------------------------------------
# iWave interfaces
# TODO: move to base class or define a new interface
# ---------------------------------------------------------


# TODO: unify with wave.get_tube_name() and move to share place
def get_tube_name(klass):
    if isinstance(klass, str):
        tube_name = klass.split(":")[-1]
    else:
        tube_name = f"{klass.__module__.replace('.', '_')}_{klass.__name__}"
    return tube_name


# TODO: Use Enum?
# class DatalakeBehavior(IntEnum):
#     ALL_RESTRICTIONS = 0
#
#
ALL_RESTRICTIONS = 0
ALLOW_DIFFERENT_STRUCTURE = 1
ALLOW_SAME_DATE_DIFFERENT_VALUES = 2
ALLOW_DUPLICATED_ITEMS = 4


class WaveStorage(iWaves, iStorage):
    "A mixing of iWave and Storage, using itself as Storage"

    def __init__(
        self,
        url="./db",
        storage: iStorage = None,
        mode=iWaves.MODE_TUBE,
        policy=DataInsertionPolicy,
    ):
        super().__init__(url=url, storage=storage, policy=policy)
        self.mode = mode

        # relax some restrictions to insert data in datalake
        # for some uri patterns
        self.behavior_templates = {}
        self.behavior_uri = {}

        # TODO: agp: load this behaviours from datalake
        behavior = ALLOW_DIFFERENT_STRUCTURE + ALLOW_SAME_DATE_DIFFERENT_VALUES
        for pattern in [
            # "centesimal://centesimal/.*MAL\d+",
            ".*://centesimal/.*",
            "turism://.*",
        ]:
            self.behavior_templates[pattern] = behavior

    async def get(self, uri: URI, cache=True) -> JSON:
        return await self.storage.get(uri)

    async def query(self, query: URI | QUERY, **params) -> List[JSON]:
        return await self.storage.query(query, **params)

    async def put(self, uri: URI, data: JSON = None, **kw) -> bool:
        """
        Try to insert a new wave object into storage:

        1. check if *same* object has been inserted in `tube` previously:
           - (within grace period)
           - if an identical object has been found, just ignore it.
           - if an object with the same `sort_key` exists in the tube warning about the differences.
           - if such *holder* object is not found in `tube` the insert it.

        2. if the object has been inserted in `tube` then:
           - create / update Snapshot
           - cteate / update Wave info with original the original query data


        e:  exists
        sv: same sort values
        st: same structure keys
        vs  same values sort

        | e   | sv  | st  | vs  | result                                            |
        | --- | --- | --- | --- | ------------------------------------------------- |
        | T   | T   | T   | T   | Skip: identical                                   |
        | T   | T   | T   | F   | Skip: EP modified same object                     |
        | T   | T   | F   | T,F | Skip: EP yield more/less data for same object     |
        | --- | --- | --- | --- | ------------------------------------------------- |
        | T   | F   | T   | T   | Skip: EP provides same object & different sort key|
        | T   | F   | T   | F   | Push: a new update of the same object             |
        | T   | F   | F   | T,F | Push: a new object and change in structure        |
        | --- | --- | --- | --- | ------------------------------------------------- |
        | F   | T,F | T,F | T,F | Push: 1st time for this object/grace period       |

        """
        # if data is None:
        #     data = kw
        # else:
        #     data.update(kw)
        data = data.copy()  # don't alter the caller item
        try:
            if self._has_change(uri, **data):
                _uri = parse_duri(uri)
                # compute some values for clarity
                namespace = _uri["fscheme"]
                database = _uri["host"]
                thing = _uri["thing"]
                uid = data.pop("id", None)
                data[ORG_KEY] = uid or _uri.get("id")  #  must exists!
                # TODO: agp: REVIEW when data[ORG_KEY] is None
                assert data[ORG_KEY], "id isn't provided?"

                monotonic = data.setdefault(MONOTONIC_KEY, monotonic_wave())
                grace_period = kw.get(GRACE_PERIOD_KEY, sys.float_info.max)
                grace_period *= 10**3  # misileconds
                since_value = monotonic - grace_period
                sort_keys = kw.get(SORT_KEY, [])
                reverse_sort_keys = kw.get(REVERSE_SORT_KEY, [])
                sort_kw_presence = all([kw.get(_) for _ in sort_keys])
                sort_data_presence = all([data.get(_) for _ in reverse_sort_keys])
                if not sort_keys or not sort_kw_presence:
                    if sort_keys:
                        log.debug(
                            "[%s] provide [%s] as sort_keys, but is not present in data: [%s], trying to find ones",
                            uri,
                            sort_keys,
                            list(data.keys()),
                        )
                    else:
                        log.debug(
                            "[%s] doesn't provide any sort_keys (i.e datetime, timestamp, etc): %s, trying to find ones",
                            uri,
                            data,
                        )
                    stream = [data]
                    # stream = [kw]
                    if not (sort_keys := SortKeyFinder.find_sort_key(stream=stream)):
                        kind = kw.get(KIND_KEY)
                        sort_keys = kw[SORT_KEY] = SortKeyFinder.get(kind)

                    kw[SORT_KEY] = sort_keys
                    log.debug("[%s] found: %s as sort_keys", uri, sort_keys)
                    if not sort_keys:
                        log.info(
                            "[%s] SortKeyFinder can't find any sort_key from: %s",
                            uri,
                            data,
                        )
                        foo = 1
                        # return

                # 1. check if *same* object has been inserted in `tube` previously:
                #     - (within grace period)
                #     - if an identical object has been found, just ignore it.
                #     - if an object with the same `sort_key` exists in the tube warning about the differences.
                #     - if such *holder* object is not found in `tube` the insert it.

                query = f"{namespace}://{database}/{thing}"

                # data_sort_blueprint = build_dict(data, sort_keys)
                data_sort_blueprint = build_dict(data, reverse_sort_keys)
                blueprint = {
                    MONOTONIC_SINCE_KEY: MONOTONIC_KEY,
                    MONOTONIC_SINCE_VALUE: since_value,
                    MONOTONIC_SINCE_OPERATOR: ">=",
                    ORDER_KEY: MONOTONIC_KEY,
                    DIRECTION_KEY: DIRECTION_DESC,
                    # LIMIT_KEY: 1,
                    ORG_KEY: uid,
                    **data_sort_blueprint,  # implies sv = True
                }
                # TODO: LIMIT 1 ?

                # MASK = set([ID_KEY, MONOTONIC_KEY, *sort_keys])
                MASK = set([ID_KEY, MONOTONIC_KEY])
                # existing = await self.storage.query(query, **blueprint)
                # N = len(existing)

                # TODO: agp: cache and get behaviour from database?
                if not (behavior := self.behavior_uri.get(query)):
                    for (
                        pattern,
                        permissions,
                    ) in self.behavior_templates.items():
                        if re.match(pattern, query):
                            behavior = permissions
                            break
                    else:
                        behavior = ALL_RESTRICTIONS

                    self.behavior_uri[query] = behavior

                existing2 = await self.storage.query(
                    query,
                    **blueprint,
                    # **data_sort_bp,
                )
                N2 = len(existing2)
                if data_sort_blueprint and N2 > 1:
                    if behavior & ALLOW_DUPLICATED_ITEMS:
                        log.info(
                            "tube [%s] has multiples records: [%s] records, but ALLOW_SAME_DATE_DIFFERENT_VALUES is defined",
                            uid,
                            N2,
                        )
                        existing2.clear()
                    else:
                        log.error(
                            "tube has multiples records: [%s] = %s records, must just 1 and sort_key is defined by: [%s]",
                            uid,
                            N2,
                            data_sort_blueprint,
                        )

                push = True
                for exists in existing2:
                    existing_sort_blueprint = build_dict(exists, reverse_sort_keys)

                    # check if stream provide an old-echo item
                    # sort_keys must exists in both data
                    old_echo = [
                        (old_echo.append(data[_] < exists[_]) if _ in exists else False)
                    ]
                    if any(old_echo):
                        log.warning(
                            "provider give old data again, preserving storage value and ignore this old_echo"
                        )
                        push = False
                        break

                    same_sort_key = existing_sort_blueprint == data_sort_blueprint

                    # check if we must "duplicate" data inside tube
                    keys0 = set(exists).difference(MASK)
                    keys1 = set(data).difference(MASK)
                    same_structure = keys0 == keys1

                    same_values = False
                    if same_sort_key and same_structure:
                        for key in keys0:
                            if exists[key] != data[key]:
                                log.warning(
                                    "[%s].[%s].[%s]: %s != %s",
                                    uid,
                                    data_sort_blueprint,
                                    key,
                                    exists[key],
                                    data[key],
                                )
                                break
                        else:
                            same_values = True

                        if not same_values:
                            log.warning(
                                "[%s].sort_keys: %s",
                                uid,
                                data_sort_blueprint,
                            )
                            log.warning("existing: %s", DATE(exists[MONOTONIC_KEY]))
                            log.warning("new data: %s", DATE(data[MONOTONIC_KEY]))
                            foo = 1
                    else:
                        same_values = False

                    # explain why object will be skipped
                    if same_sort_key:
                        # same sort_key
                        if same_structure:
                            # EP preserver known structure
                            if same_values:
                                # new object and existing one are identical
                                # including `sort_keys`
                                # object is not inserted, continue with the next one
                                log.debug(
                                    "[%s][%s]: SKIP, new and existing are identical.",
                                    uid,
                                    data_sort_blueprint,
                                )
                                push = False
                                break
                            elif data_sort_blueprint:
                                if behavior & ALLOW_SAME_DATE_DIFFERENT_VALUES:
                                    log.debug(
                                        "[%s][%s], EP send a modified version of an already sent object, but behavior has ALLOW_SAME_DATE_DIFFERENT_VALUES, so restriction is RELAXED",
                                        uid,
                                        data_sort_blueprint,
                                    )
                                else:
                                    # but EP modified an already sent object
                                    log.error(
                                        "[%s][%s], EP send a modified version of an already sent object",
                                        uid,
                                        data_sort_blueprint,
                                    )
                                    push = False
                                    break
                            else:
                                # but EP modified an already sent object
                                log.debug(
                                    "OK [%s] EP send a modified version of an already sent object, but data has't sort_keys, so must be inserted each time data is different",
                                    uid,
                                )
                                foo = 1

                        else:
                            # and EP yield more/less data for same object
                            log.warning(
                                "[%s].[%s], EP send a different structure that previous ones",
                                uid,
                                data_sort_blueprint,
                            )
                            log.warning(
                                "[%s].[%s]: existing: [%s]",
                                uid,
                                data_sort_blueprint,
                                exists,
                            )
                            log.warning(
                                "[%s].[%s]: new     : [%s]",
                                uid,
                                data_sort_blueprint,
                                data,
                            )
                            foo = 1

                    else:
                        # sort_key values differs
                        if same_structure:
                            # struct doesn't change
                            if same_values:
                                # data is unchanged but the `sort_keys`
                                log.error(
                                    "[%s]: data is unchanged but the `sort_keys`: %s <--> %s",
                                    uid,
                                    data_sort_blueprint,
                                    existing_sort_blueprint,
                                )
                                push = False
                                break
                            else:
                                # a new update of the same object
                                pass
                                # push = True
                        else:
                            # a new object with a change in its structure
                            # push = True
                            log.error(
                                "[%s].[%s]: has change its structure: [%s]",
                                uid,
                                keys0.symmetric_difference(keys1),
                            )
                    foo = 1
                else:
                    pass
                    # push = True

                if push:
                    if isinstance(self.storage, SurrealistStorage):
                        log_records.debug(
                            ">> INSERT: [%s].[%s]: %s",
                            uid,
                            data_sort_blueprint,
                            data,
                        )
                        foo = 1
                    query = f"{namespace}://{database}/{thing}:{monotonic}"
                    res2 = await self.storage.put(query, data)
                    foo = 1

                # TODO: agp: review
                # else:
                #     return True

                # long fquid version
                # data[ID_KEY] = data[ORG_KEY]
                # short version
                data[ID_KEY] = "{thing}:{id}".format_map(_uri)

                query = f"{namespace}://{database}/{TUBE_SNAPSHOT}"
                # resuming_info = {k: kw[k] for k in kw.get(REVERSE_SORT_KEY, [])}
                resuming_info = {k: kw[k] for k in kw.get(SORT_KEY) or []}

                # force to be json compatible
                resuming_info = JSONVerter.to_json(resuming_info)
                res0 = await self.storage.put(
                    query,
                    data,
                    **{
                        WAVE_RESUMING_INFO_KEY: resuming_info,
                    },
                )
                # 3. finally add the wave info into tube
                data.pop(MONOTONIC_KEY)

                # 2. save last Wave from this particular tube
                # AVOID_KEYS contains all keys that aren't json serializable
                # wave = {
                #     k: v for k, v in kw.items() if k not in self.AVOID_KEYS
                # }

                # try to recover the 'intact' bootstrap that we've using
                for wave0 in kw.get(WAVE_LAST_KEY, []):
                    wave = wave0.get("wave")  # TODO: use a define
                    if wave:
                        break
                else:
                    # otherwise, its the 1st time and we need to create the 1st
                    # bootstrap-wave info

                    # TODO: review for inclussion
                    # TODO: this settings are crawler activity oriented
                    # TODO: what about 'Task' an other use cases?
                    wave_keys = set(kw.get(WAVE_INFO_KEY, []))
                    wave_keys.update([KIND_KEY, PREFIX_URL, PARAMS_KEY])

                    # task = kw[TASK_KEY]
                    wave = {k: kw[k] for k in wave_keys.intersection(kw)}

                if wave:
                    # wave must be json compatible and do not use any reserved
                    # keyword for storage (i.e. 'scope' in Surreal)
                    query = f"{namespace}://{database}/{TUBE_WAVE}"
                    exists = await self.storage.query(query, **wave)
                    assert len(exists) <= 1

                    if len(exists):
                        # use the same record_id
                        # otherwise a new record will be created
                        wave = exists[0]
                    # stamp current wave
                    wave[MONOTONIC_KEY] = monotonic
                    res1 = await self.storage.put(query, wave)
                else:
                    # wave is empty, maybe because is not a resuming crawling task
                    log.info(
                        "wave is empty, maybe because is not a resuming crawling task"
                    )
                    log.info("Saving: %s", data)
                    res1 = True

                return all([res0, res1, res2])
            else:
                return True
        except Exception as why:  # pragma: nocover
            log.error(why)
            log.error("".join(traceback.format_exception(*sys.exc_info())))

    async def update_meta(self, tube, meta, merge=True):
        """Update the tube metadata.
        If merge is Frue, meta-data will me merge
        If merge is False, meta-data will be replace

        """
        # TODO: global for all ns?
        # TODO: then, fquid must be used, not just ID
        storage = self.storage
        # option 1: global storarage in SYSTEM namespace
        # holder = f"{TUBE_NS}://{TUBE_DB}/{TUBE_META}"

        # option 2: local to current namespace
        # so gobal search must loop over all/wanted namespaces
        _uri = parse_duri(tube)
        _uri["path"] = f"/{TUBE_META}"
        _uri["id"] = _uri.pop("_path")
        holder = build_uri(**_uri)

        # find metadata
        result = await self.find_meta(tube, meta)

        if result:
            while len(result) > 1:
                record = result.pop()
                record_id = record["id"]
                log.warning(f"removing duplicate record meta: {record_id}")
                m = REG_SPLIT_PATH.match(record_id)
                if m:
                    _id = m.groupdict()["id"]
                uri = f"{holder}:{_id}"
                res = await storage.delete(uri)
                assert res, "data hasn't been deleted!?"

            if merge:
                assert len(result) == 1
                _meta = result[0]
                if isinstance(_meta, dict):
                    if all([_meta.get(key) == meta[key] for key in meta]):
                        # don't update anything
                        # so it will not activate any live_query
                        return True
                    meta = merge_dict(_meta, meta)

            ok = await storage.put(holder, meta)
        else:
            ok = await storage.put(holder, meta)

        return ok

    async def instrospection(self):
        """
        Example:
        result
        {'namespaces': {'kraken': 'DEFINE NAMESPACE kraken',
                        'meteo': 'DEFINE NAMESPACE meteo',
                        'parking': 'DEFINE NAMESPACE parking',
                        'swarm': 'DEFINE NAMESPACE swarm',
                        'test': 'DEFINE NAMESPACE test',
                        'weather': 'DEFINE NAMESPACE weather'},
         'users': {},
         'databases': {},
         'tokens': {},
         'analyzers': {},
         'functions': {},
         'models': {},
         'params': {},
         'scopes': {},
         'tables': {}}

        """
        storage = self.storage
        universe = await storage.instrospection()
        for ns, namespace in universe.items():
            for db, database in namespace.items():
                for tb, table in database.items():
                    if tb in TUBE_TABLES:
                        continue
                    foo = 1

        # TODO: refactor meta and use simpler manner or default value
        metas = await storage.find_meta(meta={})
        for meta in metas:
            # enchamce data
            kind = meta.get(KIND_KEY, "")
            # TODO: implement
            pass

        return universe

    async def find_meta(self, tube, meta):
        """Find tubes that match the specified meta"""
        assert isinstance(tube, str), "update_meta need a tube string"

        # TODO: implement using a general query with params
        # fqid = f"{TUBE_META}:{tube}"
        # meta[ORG_KEY] = tube

        # TODO: global for all ns?
        # TODO: then, fquid must be used, not just ID
        storage = self.storage

        # option 1: global storarage in SYSTEM namespace
        # holder = f"{TUBE_NS}://{TUBE_DB}/{TUBE_META}"

        # option 2: local to current namespace
        # so gobal search must loop over all/wanted namespaces
        _uri = parse_duri(tube)
        _uri["path"] = f"/{TUBE_META}"
        _uri["id"] = _uri.pop("_path")
        holder = build_uri(**_uri)

        # query = f"{holder}?{ORG_KEY}={tube}"
        # result = await self.query(query)
        result = await storage.query(holder, **meta)

        return result

    def running(self):
        return self.storage.running()


# ---------------------------------------------------------
# Surreal Storage
# TODO: move to base class or define a new interface
# ---------------------------------------------------------


# TODO: move this definitions and DB_LAYOUT to a common place

QUERY_UPDATE_TUBE_SYNC = "UPDATE $record_id SET wave__ = $wave__;"
QUERY_SELECT_TUBE_SYNC = (
    f"SELECT * FROM {TUBE_SYNC} WHERE source=$source AND target=$target" ""
)


class SurrealConnectionPool(iConnectionPool):
    "TBD"
    MAX_HARD_CONNECTIONS = 250
    DROP_CONNECTIONS = 100
    MAX_RECONNECTION = 10

    def __init__(
        self,
        url,
        user="root",
        password="root",
        ns="test",
        db="test",
    ):
        super().__init__(url)
        self.user = user
        self.password = password
        self.ns = ns
        self.db = db
        self.surreal = None

    def close(self):
        "close connection pool"
        try:
            for key in list(self.connections):
                self._close(key)
        except Exception:
            pass

    def _close(self, key):
        conn = self.connections.pop(key)
        # print(f"dropping: {key}")
        try:
            if conn.is_connected():
                conn.close()
        except Exception:
            # surrealist.errors.OperationOnClosedConnectionError
            pass

    async def _connect(self, *key):
        connection = self.connections.get(key)
        if connection:
            namespace, database = key
            if getattr(connection, "database", None) != database:
                result = connection.use(namespace, database)
                setattr(connection, "database", database)

            return connection

        url = parse_uri(self.url)
        assert url["fscheme"] in (
            None,
            "http",
            "https",
            "ws",
        ), "bad scheme for surreal"

        if url["fscheme"] in (None,):
            url["fscheme"] = "ws"

        if url["fscheme"] in ("ws",):
            url["path"] = "/rpc"
        else:
            url["path"] = ""
        url = build_uri(**url)

        t0 = time.time()
        if self.surreal is None:
            self.surreal = Surrealist(
                url,
                # namespace=namespace,
                # database=self.db,
                credentials=(self.user, self.password),
                use_http=False,
                timeout=20,
            )
            # print(url)

        for i in range(self.MAX_RECONNECTION):
            try:
                # print(self.surreal.is_ready())
                # print(self.surreal.version())
                # print(self.surreal.health())

                connection = self.surreal.connect()

                if len(self.connections) >= self.MAX_HARD_CONNECTIONS:
                    keys = list(self.connections)
                    drops = set()
                    N = len(keys) - 1
                    while len(drops) < self.DROP_CONNECTIONS:
                        drops.add(keys[random.randint(0, N)])

                    for key in drops:
                        self._close(key)
                break
            except Exception as why:  # pragma: nocover
                print(f"[{i}] {why}")
                time.sleep(1)

        # print(f"creating: {key}: elapsed: {elapsed}")
        if connection is None:
            raise RuntimeError(f"{self} can't create a connection for: {key}")
        self.connections[key] = connection
        namespace, database = key
        result = connection.use(namespace, database)
        # setattr(connection, "database", database)
        # create initial database layout
        # await self._update_database_layout(connection)
        self.last_connection = connection
        return connection


class SurrealistStorage(Storage):

    DB_INFO = """
    INFO FOR DB;
    """
    DB_LAYOUT = {
        TUBE_META: f"""
        DEFINE TABLE IF NOT EXISTS {TUBE_META} SCHEMALESS;
        -- TODO: set an index properly
        -- TODO: the next sentence will cause an error creating records
        -- DEFINE FIELD id ON TABLE {TUBE_META};
        """,
        # TUBE_WAVE: f"""
        # DEFINE TABLE IF NOT EXISTS {TUBE_WAVE} SCHEMAFULL;
        # DEFINE FIELD id ON TABLE {TUBE_WAVE} TYPE string;
        # DEFINE FIELD wave ON TABLE {TUBE_WAVE} TYPE int;
        # """,
        TUBE_SYNC: f"""
        DEFINE TABLE IF NOT EXISTS {TUBE_SYNC} SCHEMAFULL;
        DEFINE FIELD source ON TABLE {TUBE_SYNC} TYPE string;
        DEFINE FIELD target ON TABLE {TUBE_SYNC} TYPE string;
        DEFINE FIELD {MONOTONIC_KEY} ON TABLE {TUBE_SYNC} TYPE int;
        """,
        f"{TUBE_SYNC}Index": f"""
        DEFINE INDEX IF NOT EXISTS {TUBE_SYNC}Index ON {TUBE_SYNC} COLUMNS source, target UNIQUE;
        """,
    }

    def __init__(
        self,
        url="./db",
        user="root",
        password="root",
        ns="test",
        db="test",
        policy=DataInsertionPolicy,
    ):
        super().__init__(url=url, policy=policy)

        self.connection_pool = SurrealConnectionPool(url, user, password, ns, db)

    def close(self):
        self.connection_pool.close()

    def __del__(self):
        self.close()

    async def start(self):
        "any action related to start storage operations"
        await super().start()
        # _ = self.connection or await self._connect()

    async def stop(self):
        "any action related to stop storage operations"
        await super().stop()
        self.close()

    async def query(self, query: URI | QUERY, **params) -> List[JSON]:
        "Make a query to the system based on URI (pattern)"
        _uri = parse_duri(query)
        _path = _uri["_path"]  # must exists
        table = tf(_path)

        variables = _uri.get("query_", {})
        if _sid := _uri.get(ID_KEY):
            variables.update(params)
            if variables:
                log.warning(
                    "Ignoring params: %s as query provides an ID: %s -> %s",
                    variables,
                    query,
                    _sid,
                )
            variables = {ORG_KEY: query}
            params = {
                ORDER_KEY: MONOTONIC_KEY,
                DIRECTION_KEY: DIRECTION_DESC,
                LIMIT_KEY: 1,
            }

        variables.update(params)

        order__ = variables.pop(ORDER_KEY, None)
        limit__ = variables.pop(LIMIT_KEY, None)
        direction__ = variables.pop(DIRECTION_KEY, None)
        since_key__ = variables.pop(MONOTONIC_SINCE_KEY, None)
        since_value__ = variables.pop(MONOTONIC_SINCE_VALUE, None)
        since_operator__ = variables.pop(MONOTONIC_SINCE_OPERATOR, None)
        where__ = variables.pop(WHERE_KEY, "")

        # mapping to surreal
        namespace = tf(_uri.get("fscheme", DEFAULT_NAMESPACE))
        database = tf(_uri.get("host", DEFAULT_DATABASE))
        key = namespace, database

        pool = self.connection_pool
        connection = pool.connections.get(key) or await pool._connect(*key)
        assert connection, "surreal connection has failed"

        # TODO: Work arround
        # TODO: There was a problem with the database: Parse error: Exceeded maximum parse depth
        # TODO: agp: it looks like 14 is the max number or "AND" in a sentence

        def build_sql(variables):
            if variables:
                where = "\n AND ".join(f"{k}=${k}" for k in variables)
                sql = f"SELECT * FROM {table} WHERE {where}"

            else:
                sql = f"SELECT * FROM {table}"

            return sql

        if variables:
            sql_sentences = []
            candidate_variables = {
                # TODO: REVIEW: is this is useful?
                key: value
                for key, value in variables.items()
                if re.match(r"(.*__$)|name|description|type", key)
                # if re.match(r"kind__", key)
            }
            # if used_variables:
            #     sql_sentences.append(build_sql(used_variables))

            used_variables = dict(candidate_variables)
            remain_variables = dict(variables)

            while remain_variables:
                key, value = remain_variables.popitem()
                if key not in used_variables:
                    candidate_variables[key] = value
                    if len(candidate_variables) >= 10:
                        sql_sentences.append(build_sql(candidate_variables))
                        candidate_variables.clear()
            if candidate_variables:
                sql_sentences.append(build_sql(candidate_variables))

            sql = sql_sentences.pop(0)
            for i, parent_sql in enumerate(sql_sentences):
                parent_sql = sql_sentences.pop(0)
                indent = "    " * (i + 1)
                sql = f"\n{sql}"
                sql = sql.replace("\n", f"\n{indent}")

                parent_sql = parent_sql.replace(table, f"\n( {sql}\n)\n")
                sql = parent_sql.format_map(locals())
                foo = 1
        else:
            sql = build_sql(variables)

        # while len(used_variables) < min(10, len(variables)):
        #     for key, value in variables.items():
        #         if key not in used_variables:
        #             used_variables[key] = value

        # TODO: <<<<<

        if where__:
            sql += f" WHERE {where__}"

        if since_key__:
            where__ += f" {since_key__} {since_operator__} ${since_key__}"
            variables[since_key__] = since_value__

        if order__:
            sql += f"\nORDER BY {order__}"

        if direction__:
            sql += f" {direction__}"

        if limit__:
            sql += f"\nLIMIT {limit__}"

        # Note: variables must be JSON serializable
        # don't try to convert datetimes, etc here
        # convert them from caller perspective
        res = connection.query(sql, variables=variables)
        if res.status not in ("OK",):
            raise RuntimeError(f"{res.status}: {res.result}\nSQL: {sql}")
        self.last_connection = connection
        return res.result

    async def save(self, nice=False, wait=False):
        "TBD"
        return True  # Nothig to do

    async def since(self, fqid, wave, max_results=100):

        _uri = parse_duri(fqid)

        thing = _uri["thing"]
        thing = tf(thing)
        # sql = f"""
        # SELECT *
        # FROM {thing}
        # WHERE  {MONOTONIC_KEY} > {wave}
        # ORDER BY _wave ASC
        # LIMIT {max_results}
        # """

        # Note: now, wave__ is stored as part of the object id
        # Note: so the query and the way to extract the wave later on
        # Note: is different
        sql = f"""
        SELECT *
        FROM {thing}
        WHERE {ID_KEY} > {thing}:{wave}
        ORDER BY {MONOTONIC_KEY} ASC
        LIMIT {max_results}
        """
        key = (_uri["fscheme"], _uri["host"])
        pool = self.connection_pool
        connection = pool.connections.get(key) or await pool._connect(*key)
        assert connection, "surreal connection has failed"

        res = connection.query(sql)
        return res.result

    async def _update_database_layout(self, connection):
        """
        Check / Create the expected database layout
        """
        # info = self.connection.query(self.DB_INFO)
        # tables = info.result["tables"]
        for table, schema in self.DB_LAYOUT.items():
            # TODO: check tables and individual indexes
            if True:  # or table not in tables:
                # TODO: delete # schema = "USE NS test DB test;" + schema
                result = connection.query(schema)
                if result.status in ("OK",):
                    log.info("[%s] : %s", schema, result.status)
                else:
                    log.error("[%s] : %s", schema, result.status)

    async def update_meta(self, tube, meta, merge=True):
        """Update the tube metadata.
        If merge is Frue, meta-data will me merge
        If merge is False, meta-data will be replace
        """
        # TODO: move out to Wavestorage or iStorage?
        assert isinstance(tube, str), "update_meta need a tube string"
        # fqid = f"{TUBE_META}:{tube}"
        meta[ORG_KEY] = tube

        # TODO: global for all ns?
        # TODO: then, fquid must be used, not just ID
        holder = f"{TUBE_NS}://{TUBE_DB}/{TUBE_META}"
        query = f"{holder}?{ORG_KEY}={tube}"
        result = await self.query(query)

        if result:
            if merge:
                assert len(result) == 1
                _meta = result[0]
                if isinstance(_meta, dict):
                    if all([_meta.get(key) == meta[key] for key in meta]):
                        # don't update anything
                        # so it will not activate any live_query
                        return True
                    meta = merge_dict(_meta, meta)

            ok = await self.put(holder, meta)
        else:
            ok = await self.put(holder, meta)

        return ok

    async def find_meta(self, meta):
        """Find tubes that match the specified meta"""
        # if not meta:
        #     raise RuntimeError(f"meta can't be empty")

        params = " AND ".join([f"{key}=${key}" for key in meta])
        if params:
            query = f"SELECT * FROM {TUBE_META} WHERE {params}"
        else:
            query = f"SELECT * FROM {TUBE_META}"

        key = TUBE_NS, TUBE_DB
        pool = self.connection_pool
        connection = pool.connections.get(key) or await pool._connect(*key)
        assert connection, "surreal connection has failed"

        res = connection.query(
            query,
            meta,
        )
        if res.status in ("OK",):
            return res.result
        raise RuntimeError(f"bad query: {query}")

    async def info(self, uri="", structured=False):
        "TBD"
        # _uri = parse_duri(uri, _normalize_=["fscheme", "host"])
        _uri = parse_uri(uri)
        key = _uri["fscheme"] or "", _uri["host"] or ""
        pool = self.connection_pool
        connection = pool.connections.get(key) or await pool._connect(*key)
        assert connection, "surreal connection has failed"

        result = {}
        functions = []

        if key[0]:
            if key[1]:
                functions.append("db")
            else:
                functions.append("ns")
        else:
            functions.append("root")

        for func in functions:
            result.update(
                getattr(connection, f"{func}_info")(structured=structured).result
            )

        return result

    async def instrospection(self):
        """
        Example:
        result
        {'namespaces': {'kraken': 'DEFINE NAMESPACE kraken',
                        'meteo': 'DEFINE NAMESPACE meteo',
                        'parking': 'DEFINE NAMESPACE parking',
                        'swarm': 'DEFINE NAMESPACE swarm',
                        'test': 'DEFINE NAMESPACE test',
                        'weather': 'DEFINE NAMESPACE weather'},
         'users': {},
         'databases': {},
         'tokens': {},
         'analyzers': {},
         'functions': {},
         'models': {},
         'params': {},
         'scopes': {},
         'tables': {}}

        """

        universe = {}
        root = await self.info(structured=False)

        for ns_name in root["namespaces"]:
            namespace = universe.setdefault(ns_name, {})
            ns_info = await self.info(f"{ns_name}://")
            for db_name in ns_info["databases"]:

                database = namespace.setdefault(db_name, {})
                db_info = await self.info(f"{ns_name}://{db_name}")
                database.update(db_info["tables"])
                # for table_name, table_info in db_info["tables"].items():
                #     database[table_name] = table_info

        return universe

    async def count(self, table):
        _uri = parse_duri(table, _normalize_=".*")
        key = _uri["fscheme"], _uri["host"]
        pool = self.connection_pool
        connection = pool.connections.get(key) or await pool._connect(*key)
        assert connection, "surreal connection has failed"
        table = _uri["thing"]

        result = connection.count(table)
        return result.result
