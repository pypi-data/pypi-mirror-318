from pathlib import Path

import pytest
from seJsonDB.db import JsonDB


def test_stats_file_with_data(tmpdir):
    test_file = tmpdir.join("test_with_data.json")
    test_file.write('{"data": {"1": {"name": "item1"}, "2": {"name": "item2"}}}')
    db = JsonDB(test_file.strpath)
    stats = db.stats()
    assert stats == {"Count": 2}


def test_stats_file_no_data(tmpdir):
    test_file = tmpdir.join("test_no_data.json")
    test_file.write('{"data": {}}')
    db = JsonDB(test_file.strpath)
    stats = db.stats()
    assert stats == {"Count": 0}


def test_stats_file_missing_data_section(tmpdir):
    test_file = tmpdir.join("test_missing_data_section.json")
    test_file.write('{}')
    db = JsonDB(test_file.strpath)
    with pytest.raises(KeyError):
        stats = db.stats()


def test_stats_non_dict_data_structure(tmpdir):
    test_file = tmpdir.join("test_non_dict_data_structure.json")
    test_file.write('{"data": ["item1", "item2"]}')
    db = JsonDB(test_file.strpath)
    stats = db.stats()
    assert stats == {}