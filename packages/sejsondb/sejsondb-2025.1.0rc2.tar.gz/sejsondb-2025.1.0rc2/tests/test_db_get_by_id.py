import json

import pytest
from seJsonDB.db import JsonDB
from seJsonDB.errors import IdDoesNotExistError, SchemaTypeError

TEST_DATA = {
    "data": {
        "123456": {"name": "John Doe", "age": 30},
        "987654": {"name": "Jane Smith", "age": 25}
    }
}


@pytest.fixture
def setup_test_db(tmpdir):
    db_file = tmpdir.join('test.json')
    db_file.write(json.dumps(TEST_DATA))
    return JsonDB(db_file.strpath)


def test_get_by_id_valid(setup_test_db):
    db = setup_test_db
    result = db.get_by_id("123456")
    assert result == {"name": "John Doe", "age": 30}


def test_get_by_id_invalid(setup_test_db):
    db = setup_test_db
    with pytest.raises(IdDoesNotExistError):
        db.get_by_id("000000")


def test_get_by_id_invalid_type(setup_test_db):
    db = setup_test_db
    with pytest.raises(TypeError):
        db.get_by_id(123456)  # Passing integer instead of string


def test_get_by_id_schema_error(setup_test_db, tmpdir):
    invalid_data = {
        "data": ["invalid_list"]
    }
    db_file = tmpdir.join('invalid_data.json')
    db_file.write(json.dumps(invalid_data))
    db = JsonDB(db_file.strpath)
    with pytest.raises(SchemaTypeError):
        db.get_by_id("123456")