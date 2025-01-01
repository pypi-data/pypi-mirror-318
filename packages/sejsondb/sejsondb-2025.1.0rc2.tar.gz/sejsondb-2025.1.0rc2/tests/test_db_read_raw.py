import json

import pytest
from seJsonDB.db import JsonDB

TEST_RAW_DATA = {
    "123": {"name": "user1", "age": 25},
    "456": {"name": "user2", "age": 30}
}


def test_read_raw_data(tmpdir):
    test_file = tmpdir.join("test.json")
    test_file.write(json.dumps(TEST_RAW_DATA))
    db = JsonDB(test_file.strpath)
    assert db.read_raw_data() == TEST_RAW_DATA
