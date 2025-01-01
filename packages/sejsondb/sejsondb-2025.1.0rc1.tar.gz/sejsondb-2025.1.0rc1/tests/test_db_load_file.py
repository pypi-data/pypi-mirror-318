import json

import pytest
import ujson
from seJsonDB.db import JsonDB
from seJsonDB.errors import SchemaError


@pytest.fixture
def mock_jsondb_with_file(tmp_path):
    test_file = tmp_path / "test_db.json"
    test_file.write_text('{"key": "value"}')
    return str(test_file)


@pytest.fixture
def mock_jsondb_with_ujson_file(tmp_path):
    test_file = tmp_path / "test_db_ujson.json"
    test_file.write_text('{"key": "value"}')
    return str(test_file)


def test_load_file_with_auto_update_enabled(mock_jsondb_with_file):
    db = JsonDB(mock_jsondb_with_file, auto_update=True, ujson=False)
    loaded_data = db._load_file()
    assert loaded_data == {"key": "value"}


def test_load_file_with_auto_update_enabled_ujson(mock_jsondb_with_ujson_file):
    db = JsonDB(mock_jsondb_with_ujson_file, auto_update=True, ujson=True)
    loaded_data = db._load_file()
    assert loaded_data == {"key": "value"}


def test_load_file_with_auto_update_disabled():
    db = JsonDB("", auto_update=False, ujson=False, load_json={"key": "value"})
    loaded_data = db._load_file()
    assert loaded_data == {"key": "value"}


def test_load_file_invalid_json(tmp_path):
    invalid_json_file = tmp_path / "invalid.json"
    invalid_json_file.write_text("{ invalid json }")

    db = JsonDB(str(invalid_json_file), auto_update=True, ujson=False)

    with pytest.raises(json.JSONDecodeError):
        db._load_file()


def test_load_file_invalid_ujson(tmp_path):
    invalid_ujson_file = tmp_path / "invalid_ujson.json"
    invalid_ujson_file.write_text("{ invalid ujson }")

    db = JsonDB(str(invalid_ujson_file), auto_update=True, ujson=True)

    with pytest.raises(ValueError):
        db._load_file()
