import json
import uuid
import re
from copy import deepcopy
from pathlib import Path
from threading import Lock
from typing import List, Optional, Union, Pattern

from .db_types import DBSchemaType, NewKeyValidTypes, SingleDataType, ReturnWithIdType, QueryType, NewDataType, NewExDataType
from .errors import IdDoesNotExistError, SchemaTypeError, IdAllReadyExistError, SchemaError

# https://dollardhingra.com/blog/python-json-benchmarking
try:
    import ujson
    UJSON = True
except ImportError: # pragma: NotTested
    UJSON = False


class JsonDB:

    def __init__(self, filename: str, auto_update: bool = True, indent: int = 4, ujson: bool = None, load_json: DBSchemaType = None) -> None:
        self.filename = filename
        self.auto_update = auto_update
        self._au_memory: DBSchemaType = {'keys': [], 'data': {}}
        self.indent = indent
        self.lock = Lock()

        self.ujson = UJSON if ujson is None else ujson

        if load_json is not None:
            self._au_memory = load_json
            self.auto_update = False

        self._gen_db_file()

    def _load_file(self) -> DBSchemaType:
        if self.auto_update:
            with open(self.filename, encoding='utf-8', mode='r') as f:
                if self.ujson:
                    return ujson.load(f)
                else:
                    return json.load(f)
        else:
            return deepcopy(self._au_memory)

    def _dump_file(self, data: DBSchemaType) -> None:
        if self.auto_update:
            with open(self.filename, encoding='utf-8', mode='w') as f:
                if self.ujson:
                    ujson.dump(data, f, indent=self.indent)
                else:
                    json.dump(data, f, indent=self.indent)
        else:
            self._au_memory = deepcopy(data)
        return None

    def _gen_db_file(self) -> None:
        if self.auto_update:
            if not Path(self.filename).is_file():
                self.lock.acquire()
                self._dump_file(
                    {'keys': [], 'data': {}}
                )
                self.lock.release()

    @staticmethod
    def _gen_id() -> str:
        # generates a random 18 digit uuid
        return str(uuid.uuid4())

    def force_load(self) -> None:
        """
        Used when the data from a file needs to be loaded when auto update is turned off.
        """
        if not self.auto_update:
            self.auto_update = True
            self._au_memory = self._load_file()
            self.auto_update = False

    def commit(self) -> None:
        if not self.auto_update:
            self.auto_update = True
            self._dump_file(self._au_memory)
            self.auto_update = False

    def stats(self) -> dict:
        res = {}
        with self.lock:
            data = self._load_file()['data']
            if isinstance(data, dict):
                res = {"Count": len(data)}
        return res

    def add(self, data: object) -> str:
        if not isinstance(data, dict):
            raise TypeError(f'data must be of type dict and not {type(data)}')

        with self.lock:
            db_data = self._load_file()

            keys = db_data['keys']
            if not isinstance(keys, list):
                raise SchemaTypeError(f"keys must be of type 'list' and not {type(keys)}")
            if len(keys) == 0:
                db_data['keys'] = sorted(list(data.keys()))
            else:
                if not sorted(keys) == sorted(data.keys()):
                    raise SchemaError(
                        f'Unrecognized / missing key(s) {set(keys) ^ set(data.keys())}'
                        '(Either the key(s) does not exists in the DB or is missing in the given data)'
                    )

            # ToDO: Need to add unit test to see if code is ever hit
            # if not isinstance(db_data['data'], dict):
            #     raise SchemaTypeError('data key in the db must be of type "dict"')

            if "key" in data:
                _id = data['key']
            elif "Key" in data:
                _id = data['Key']
                if _id == "00000000-0000-0000-0000-000000000000":
                    _id = str(self._gen_id())
                    data['Key'] = _id
            else:
                _id = str(self._gen_id())

            if _id not in db_data['data']:
                db_data['data'][_id] = data
                self._dump_file(db_data)
                return _id
            else:
                raise IdAllReadyExistError(f'Id `{_id}` already in DB')

    def add_many(self, data: list, json_response: bool = True) -> tuple[Union[NewDataType, None], Union[NewExDataType, None]]:
        """
        Add multiple data entries and handle various exceptions during the process. The method
        attempts to add each entry from the input list `data`, and in case of exceptions, logs the
        errors in a structured form in the returned `ex_data`. Optionally, the method can provide
        a JSON-like response for both successful and failed entries based on the `json_response`
        flag.

        :param data: A list of data entries to be processed and added.
        :type data: list
        :param json_response: A flag indicating if the response should be JSON-formatted. Defaults to True.
        :type json_response: bool
        :return: A tuple containing two dictionaries. The first dictionary (`new_data`) holds the new
            successfully added data entries mapped by their ID. The second dictionary (`ex_data`) contains
            details about any exceptions and the associated data causing them if `json_response` is True.
            If `json_response` is False, the second dictionary in the tuple is `None`.
        :rtype: tuple[Union[NewDataType, None], Union[NewExDataType, None]]
        """
        new_data = {}
        ex_data = {}

        for d in data:
            try:
                _id = self.add(d)

            except SchemaError as e:
                if json_response:
                    ex_data[len(ex_data)] = {"SchemaError": f'{e}', "data": d}
            except Exception as e:
                if json_response:
                    ex_data[len(ex_data)] = {"Exception": f'{e}', "data": d}

            else:
                if json_response:
                    new_data[_id] = self.get_by_id(_id)

        # logger.info(f'New Data: {json.dumps(new_data)}')
        # logger.error(f'Ex Data: {json.dumps(ex_data)}')
        return new_data, ex_data if json_response else None

    def get_all(self) -> ReturnWithIdType:
        data = {}
        with self.lock:
            oData = self._load_file()['data']
            if isinstance(oData, dict):
                data = oData
        return data

    def get_by_id(self, id: str) -> SingleDataType:
        if not isinstance(id, str):
            raise TypeError(f'id must be of type "str" and not {type(id)}')

        with self.lock:
            data = self._load_file()['data']
            if isinstance(data, dict):
                if id in data:
                    return data[id]
                else:
                    raise IdDoesNotExistError(f'{id!r} does not exists in the DB')
            else:
                raise SchemaTypeError('"data" key in the DB must be of type dict')

    def get_by_query(self, query: QueryType) -> ReturnWithIdType:
        if not callable(query):
            raise TypeError(f'"query" must be a callable and not {type(query)!r}')

        with self.lock:
            new_data: ReturnWithIdType = {}
            data = self._load_file()['data']
            if isinstance(data, dict):
                for id, values in data.items():
                    if isinstance(values, dict):
                        if query(values):
                            new_data[id] = values

            return new_data

    def get_by_search(self, key: str, _re: Union[str, Pattern[str]]) -> tuple[list[dict[str, int | str | bool]], int]:

        pattern = _re
        if not isinstance(_re, re.Pattern):
            pattern = re.compile(str(_re))

        items = []
        data = self.get_all()

        for d in data:
            for k, v in data[d].items():
                if k == key and re.search(pattern, v):
                    items.append(data[d])
                    continue

        return items, len(items)

    def update_by_id(self, id: str, new_data: object) -> SingleDataType:
        if not isinstance(new_data, dict):
            raise TypeError(f'new_data must be of type dict and not {type(new_data)!r}')

        with self.lock:
            data = self._load_file()
            keys = data['keys']

            if isinstance(keys, list):
                if not all(i in keys for i in new_data):
                    raise SchemaError(f'Unrecognized key(s) {[i for i in new_data if i not in keys]}')

            # if not isinstance(data['data'], dict):
            #     raise SchemaTypeError('the value for the data keys in the DB must be of type dict')

            if id not in data['data']:
                raise IdDoesNotExistError(f'The id {id!r} does noe exists in the DB')

            data['data'][id] = {**data['data'][id], **new_data}

            self._dump_file(data)
            return data['data'][id]

    def update_by_query(self, query: QueryType, new_data: object) -> List[str]:
        if not callable(query):
            raise TypeError(f'"query" must be a callable and not {type(query)!r}')

        if not isinstance(new_data, dict):
            raise TypeError(f'"new_data" must be of type dict and not f{type(new_data)!r}')

        with self.lock:
            updated_keys = []
            db_data = self._load_file()
            keys = db_data['keys']

            if isinstance(keys, list):
                if not all(i in keys for i in new_data):
                    raise SchemaError(f'Unrecognized / missing key(s) {[i for i in new_data if i not in keys]}')

            # if not isinstance(db_data['data'], dict):
            #     raise SchemaTypeError('The data key in the DB must be of type dict')

            for key, value in db_data['data'].items():
                if query(value):
                    db_data['data'][key] = {**db_data['data'][key], **new_data}
                    updated_keys.append(key)

            self._dump_file(db_data)
            return updated_keys

    def delete_by_id(self, id: str) -> bool:
        with self.lock:
            data = self._load_file()
            if not isinstance(data['data'], dict):
                raise SchemaTypeError('"data" key in the DB must be of type dict')
            if id not in data['data']:
                raise IdDoesNotExistError(f'ID {id} does not exists in the DB')
            del data['data'][id]

            self._dump_file(data)
            return True

    def delete_by_query(self, query: QueryType) -> List[str]:
        if not callable(query):
            raise TypeError(f'"query" must be a callable and not {type(query)!r}')

        with self.lock:
            data = self._load_file()
            if not isinstance(data['data'], dict):
                raise SchemaTypeError('"data" key in the DB must be of type dict')
            ids_to_delete = []
            for id, value in data['data'].items():
                if query(value):
                    ids_to_delete.append(id)
            for id in ids_to_delete:
                del data['data'][id]

            self._dump_file(data)
            return ids_to_delete

    def purge(self) -> None:
        with self.lock:
            data = self._load_file()
            if not isinstance(data['data'], dict):
                raise SchemaTypeError('"data" key in the DB must be of type dict')

            if not isinstance(data['keys'], list):
                raise SchemaTypeError('"key" key in the DB must be of type dict')
            data['data'] = {}
            data['keys'] = []
            self._dump_file(data)

    def add_new_key(self, key: str, default: Optional[NewKeyValidTypes] = None) -> bool:

        if default is not None:
            if not isinstance(default, (list, str, int, bool, dict)):
                raise TypeError(
                    f'default field must be of any of (list, int, str, bool, dict) but for {type(default)}')

        with self.lock:
            data = self._load_file()

            if key in data['keys']:
                raise KeyError(f"Key {key} already exists in DB")

            if isinstance(data['keys'], list):
                data['keys'].append(key)
                data['keys'].sort()

            if isinstance(data['data'], dict):
                for d in data['data'].values():
                    d[key] = default

            self._dump_file(data)

            return True

    def delete_key(self, key: str) -> bool:
        with self.lock:
            data = self._load_file()

            if key not in data['keys']:
                raise KeyError(f"Key {key} does not exists in DB")
            else:
                if isinstance(data['keys'], list):
                    data['keys'].remove(key)
                    data['keys'].sort()

            for d in data['data'].values():
                del d[key]

            self._dump_file(data)

            return True

    def read_raw_data(self) -> DBSchemaType:
        """Loads and returns the raw JSON data stored in the database file."""
        return self._load_file()
