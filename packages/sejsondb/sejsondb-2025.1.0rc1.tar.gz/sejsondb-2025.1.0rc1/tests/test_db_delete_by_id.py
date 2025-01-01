import json
from copy import deepcopy
from typing import Any
from typing import Dict

import pytest

from seJsonDB.db import JsonDB
from seJsonDB.errors import IdDoesNotExistError, SchemaTypeError

TEST_DATA = {
    'keys': [
        'age',
        'name',
        'place'
    ],
    'data': {
        '219520953066905460': {
            'name': 'ad0',
            'age': 0,
            'place': 'US'
        },
        '110180374400879352': {
            'name': 'ad1',
            'age': 1,
            'place': 'US'
        },
        '224980674034561069': {
            'name': 'ad2',
            'age': 74574654,
            'place': 'UK'
        },
        '228563587602913112': {
            'name': 'ad3',
            'age': 3,
            'place': 'UK'
        },
        '167833310760833974': {
            'name': 'ad5',
            'age': 4,
            'place': 'IN'
        }
    }
}


def test_delete_by_id(tmpdir):
    final_data: Dict[str, Any] = deepcopy(TEST_DATA)
    del final_data['data']['110180374400879352']

    f = tmpdir.join('test.json')
    f.write(json.dumps(TEST_DATA))
    db = JsonDB(f.strpath)

    db.delete_by_id('110180374400879352')
    assert json.loads(f.read()) == final_data


def test_delete_by_id_id_not_found_error(tmpdir):
    f = tmpdir.join('test.json')
    f.write(json.dumps(TEST_DATA))
    db = JsonDB(f.strpath)

    with pytest.raises(IdDoesNotExistError):
        db.delete_by_id('2345')


def test_delete_by_id_invalid_schema(tmpdir):
    f = tmpdir.join("test.json")
    invalid_data = {
        "data": [
            {"id": "12345", "name": "Alice", "age": 30}
        ]
    }
    f.write(json.dumps(invalid_data, indent=4))
    db = JsonDB(f.strpath)

    with pytest.raises(SchemaTypeError):
        db.delete_by_id("12345")
