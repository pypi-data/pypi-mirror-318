import json

import pytest
from seJsonDB.db import JsonDB
from seJsonDB.errors import IdDoesNotExistError, SchemaError

TEST_DATA = {
    "keys": ["name", "age"],
    "data": {
        "123456": {"name": "Alice", "age": 25},
        "234567": {"name": "Bob", "age": 30}
    }
}


@pytest.fixture
def json_db(tmpdir):
    f = tmpdir.join("test.json")
    f.write(json.dumps(TEST_DATA))
    return JsonDB(f.strpath)


def test_update_by_id_success(json_db):
    updated_data = {"age": 35}
    result = json_db.update_by_id("123456", updated_data)
    assert result == {"name": "Alice", "age": 35}


def test_update_by_id_id_not_exist(json_db):
    updated_data = {"age": 35}
    with pytest.raises(IdDoesNotExistError):
        json_db.update_by_id("999999", updated_data)


def test_update_by_id_schema_error(json_db):
    updated_data = {"location": "New York"}
    with pytest.raises(SchemaError):
        json_db.update_by_id("123456", updated_data)


def test_update_by_id_type_error(json_db):
    updated_data = ["invalid", "data"]
    with pytest.raises(TypeError):
        json_db.update_by_id("123456", updated_data)


def test_update_by_id_partial_update(json_db):
    updated_data = {"age": 26}
    result = json_db.update_by_id("123456", updated_data)
    assert result == {"name": "Alice", "age": 26}
