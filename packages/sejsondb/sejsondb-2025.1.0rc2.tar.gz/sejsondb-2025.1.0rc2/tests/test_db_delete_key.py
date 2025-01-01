import json

import pytest
from seJsonDB.db import JsonDB
from seJsonDB.errors import SchemaError


def test_delete_key_success(tmpdir, mocker):
    # Set up a database with test keys and data
    f = tmpdir.join('test.json')
    initial_data = {
        "keys": ["key1", "key2"],
        "data": {
            "id1": {"key1": "value1", "key2": "value2"},
            "id2": {"key1": "value3", "key2": "value4"}
        }
    }
    f.write(json.dumps(initial_data))
    db = JsonDB(f.strpath)

    # Delete an existing key
    assert db.delete_key("key1") is True

    # Verify the key is removed from the keys list and all data entries
    updated_data = json.loads(f.read())
    assert "key1" not in updated_data["keys"]
    for item in updated_data["data"].values():
        assert "key1" not in item


def test_delete_key_not_exists(tmpdir):
    # Set up a database with test keys and data
    f = tmpdir.join('test.json')
    initial_data = {
        "keys": ["key1", "key2"],
        "data": {
            "id1": {"key1": "value1", "key2": "value2"},
            "id2": {"key1": "value3", "key2": "value4"}
        }
    }
    f.write(json.dumps(initial_data))
    db = JsonDB(f.strpath)

    # Attempt deleting a non-existent key
    with pytest.raises(KeyError, match="Key key3 does not exists in DB"):
        db.delete_key("key3")


def test_delete_key_empty_keys(tmpdir):
    # Set up a database with an empty keys list
    f = tmpdir.join('test.json')
    initial_data = {
        "keys": [],
        "data": {}
    }
    f.write(json.dumps(initial_data))
    db = JsonDB(f.strpath)

    # Attempt deleting a key when keys list is empty
    with pytest.raises(KeyError, match="Key key1 does not exists in DB"):
        db.delete_key("key1")


def test_delete_key_schema_error(tmpdir, mocker):
    # Set up a database with an invalid schema (e.g., `keys` is not a list)
    f = tmpdir.join('test.json')
    initial_data = {
        "keys": {"key1": "value1"},
        "data": {}
    }
    f.write(json.dumps(initial_data))
    db = JsonDB(f.strpath)

    # Ensure KeyError is raised for invalid schema
    with pytest.raises(KeyError):
        db.delete_key("key2")
