from pathlib import Path

import pytest
from seJsonDB.db import JsonDB


def test_jsondb_initialization_with_valid_filename(tmpdir):
    test_file = tmpdir.join("test.json")
    db = JsonDB(test_file.strpath)
    assert db.filename == test_file.strpath
    assert db.auto_update is True
    assert db.indent == 4
    assert isinstance(db.lock, type(db.lock.__class__()))


def test_jsondb_initialization_with_auto_update_disabled(tmpdir):
    test_file = tmpdir.join("test.json")
    db = JsonDB(test_file.strpath, auto_update=False)
    assert db.auto_update is False


def test_jsondb_initialization_with_custom_indent(tmpdir):
    test_file = tmpdir.join("test.json")
    db = JsonDB(test_file.strpath, indent=2)
    assert db.indent == 2


def test_jsondb_initialization_with_ujson_enabled(tmpdir):
    test_file = tmpdir.join("test.json")
    db = JsonDB(test_file.strpath, ujson=True)
    assert db.ujson is True


def test_jsondb_initialization_with_ujson_disabled(tmpdir):
    test_file = tmpdir.join("test.json")
    db = JsonDB(test_file.strpath, ujson=False)
    assert db.ujson is False


def test_jsondb_initialization_with_load_json(tmpdir):
    test_file = tmpdir.join("test.json")
    load_json_data = {"keys": ["name", "age"], "data": {"1": {"name": "test", "age": 25}}}
    db = JsonDB(test_file.strpath, load_json=load_json_data)
    assert db._au_memory == load_json_data
    assert db.auto_update is False


def test_jsondb_gen_db_file_called_on_initialization(mocker, tmpdir):
    test_file = tmpdir.join("test.json")
    mock_gen_db_file = mocker.patch("seJsonDB.db.JsonDB._gen_db_file")
    JsonDB(test_file.strpath)
    mock_gen_db_file.assert_called_once()
