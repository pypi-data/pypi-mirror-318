import json
import re

import pytest
from seJsonDB.db import JsonDB

TEST_DATA = {"data": {
    "1": {"name": "Jane Doe", "age": 30, "city": "New York"},
    "2": {"name": "John Smith", "age": 25, "city": "Los Angeles"},
    "3": {"name": "Alice Johnson", "age": 35, "city": "Chicago"},
}}


def test_get_by_search_key_found(tmpdir):
    f = tmpdir.join("test.json")
    f.write(json.dumps(TEST_DATA, indent=4))
    db = JsonDB(f.strpath)
    result, count = db.get_by_search("name", "Jane")
    assert count == 1
    assert len(result) == 1
    assert result[0] == {"name": "Jane Doe", "age": 30, "city": "New York"}

def test_get_by_search_key_not_found(tmpdir):
    f = tmpdir.join("test.json")
    f.write(json.dumps(TEST_DATA, indent=4))
    db = JsonDB(f.strpath)
    result, count = db.get_by_search("name", "Michael")
    assert count == 0
    assert result == []


def test_get_by_search_multiple_matches(tmpdir):
    f = tmpdir.join("test.json")
    f.write(json.dumps(TEST_DATA, indent=4))
    db = JsonDB(f.strpath)
    result, count = db.get_by_search("city", "New|Los")
    assert count == 2
    assert len(result) == 2
    assert result[0] == {"name": "Jane Doe", "age": 30, "city": "New York"}
    assert result[1] == {"name": "John Smith", "age": 25, "city": "Los Angeles"}


def test_get_by_search_with_regex(tmpdir):
    f = tmpdir.join("test.json")
    f.write(json.dumps(TEST_DATA, indent=4))
    db = JsonDB(f.strpath)
    regex = re.compile(r"^J.*e$")
    result, count = db.get_by_search("name", regex)
    assert count == 1
    assert len(result) == 1
    assert result[0] == {"name": "Jane Doe", "age": 30, "city": "New York"}


def test_get_by_search_key_missing_in_data(tmpdir):
    f = tmpdir.join("test.json")
    f.write(json.dumps(TEST_DATA, indent=4))
    db = JsonDB(f.strpath)
    result, count = db.get_by_search("nickname", "anything")
    assert count == 0
    assert result == []
