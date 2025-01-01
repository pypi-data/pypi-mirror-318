import json
from pathlib import Path

import pytest
from seJsonDB.db import JsonDB
from seJsonDB.errors import SchemaTypeError

TEST_DB_CONTENT_VALID = {
    "data": {"1": {"name": "Test", "value": 123}, "2": {"name": "Another", "value": 456}},
    "keys": ["name", "value"]
}

TEST_DB_CONTENT_INVALID_DATA = {
    "data": [],
    "keys": ["name", "value"]
}

TEST_DB_CONTENT_INVALID_KEYS = {
    "data": {"1": {"name": "Test", "value": 123}},
    "keys": "not_a_list"
}


def test_purge_valid_data(tmpdir):
    file_path = tmpdir.join("test_db.json")
    file_path.write(json.dumps(TEST_DB_CONTENT_VALID, indent=4))
    db = JsonDB(file_path.strpath)

    db.purge()

    with file_path.open() as f:
        data = json.load(f)

    assert data["data"] == {}
    assert data["keys"] == []


def test_purge_invalid_data_raises_error(tmpdir):
    file_path = tmpdir.join("test_db_invalid_data.json")
    file_path.write(json.dumps(TEST_DB_CONTENT_INVALID_DATA, indent=4))
    db = JsonDB(file_path.strpath)

    with pytest.raises(SchemaTypeError, match='"data" key in the DB must be of type dict'):
        db.purge()


def test_purge_invalid_keys_raises_error(tmpdir):
    file_path = tmpdir.join("test_db_invalid_keys.json")
    file_path.write(json.dumps(TEST_DB_CONTENT_INVALID_KEYS, indent=4))
    db = JsonDB(file_path.strpath)

    with pytest.raises(SchemaTypeError, match='"key" key in the DB must be of type dict'):
        db.purge()
