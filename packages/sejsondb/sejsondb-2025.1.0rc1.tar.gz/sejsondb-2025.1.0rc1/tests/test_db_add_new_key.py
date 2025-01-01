import json

import pytest

from seJsonDB.db import JsonDB


# TEST_DATA = {
#     'version': 2,
#     'keys': ['age', 'name'],
#     'data': {
#         '2352346': {
#             'age': 4,
#             'name': 'mathew_first'
#         },
#         '1234567': {
#             'age': 9,
#             'name': 'new_user'
#         }
#     }
# }
#
#
# def test_add_new_key(tmpdir):
#
#     DATA_SUCCESS = {
#         'version': 2,
#         'keys': ['age', 'name', 'place'],
#         'data': {
#             '2352346': {
#                 'age': 4,
#                 'name': 'mathew_first',
#                 'place': 'GB'
#             },
#             '1234567': {
#                 'age': 9,
#                 'name': 'new_user',
#                 'place': 'GB'
#             }
#         }
#     }
#
#     f = tmpdir.join('test.json')
#     f.write(json.dumps(TEST_DATA))
#     db = JsonDB(f.strpath)
#     db.add_new_key('place', 'GB')
#
#     assert json.loads(f.read()) == DATA_SUCCESS
#
#
# def test_add_new_key_no_default(tmpdir):
#     DATA_SUCCESS = {
#         'version': 2,
#         'keys': ['age', 'name', 'place'],
#         'data': {
#             '2352346': {
#                 'age': 4,
#                 'name': 'mathew_first',
#                 'place': None
#             },
#             '1234567': {
#                 'age': 9,
#                 'name': 'new_user',
#                 'place': None
#             }
#         }
#     }
#
#     f = tmpdir.join('test.json')
#     f.write(json.dumps(TEST_DATA))
#     db = JsonDB(f.strpath)
#     db.add_new_key('place')
#
#     assert json.loads(f.read()) == DATA_SUCCESS
#
#
# @pytest.mark.parametrize(
#     'default',
#     (
#         (1,),
#         type('test', (), {}),
#     )
# )
# def test_add_new_key_invalid_data_type(tmpdir, default):
#     f = tmpdir.join('test.json')
#     f.write(json.dumps(TEST_DATA))
#     db = JsonDB(f.strpath)
#
#     with pytest.raises(TypeError):
#         db.add_new_key(default)


import pytest
from seJsonDB.db import JsonDB
from seJsonDB.errors import IdAllReadyExistError


def test_add_new_key_success(tmpdir, mocker):
    mocker.patch('seJsonDB.db.JsonDB._load_file', return_value={"keys": [], "data": {}})
    mocker.patch('seJsonDB.db.JsonDB._dump_file')
    f = tmpdir.join("test.json")
    db = JsonDB(f.strpath)

    result = db.add_new_key("new_key", default="default_value")

    assert result is True


def test_add_new_key_already_exists(tmpdir, mocker):
    mocker.patch('seJsonDB.db.JsonDB._load_file', return_value={"keys": ["existing_key"], "data": {}})
    mocker.patch('seJsonDB.db.JsonDB._dump_file')
    f = tmpdir.join("test.json")
    db = JsonDB(f.strpath)

    with pytest.raises(KeyError, match="Key existing_key already exists in DB"):
        db.add_new_key("existing_key")


def test_add_new_key_invalid_default_type(tmpdir, mocker):
    f = tmpdir.join("test.json")
    db = JsonDB(f.strpath)

    with pytest.raises(TypeError, match="default field must be of any of"):
        db.add_new_key("new_key", default=set())


def test_add_new_key_with_default_value(tmpdir, mocker):
    mocker.patch(
        'seJsonDB.db.JsonDB._load_file',
        return_value={
            "keys": [],
            "data": {
                "1": {"name": "John"},
                "2": {"name": "Bill"}
            }
        },
    )
    mocker.patch('seJsonDB.db.JsonDB._dump_file')
    f = tmpdir.join("test.json")
    db = JsonDB(f.strpath)

    result = db.add_new_key("age", default=30)

    assert result is True


def test_add_new_key_no_default_value(tmpdir, mocker):
    mocker.patch(
        'seJsonDB.db.JsonDB._load_file',
        return_value={
            "keys": [],
            "data": {
                "1": {"name": "Alice"},
                "2": {"name": "Bob"}
            }
        },
    )
    mocker.patch('seJsonDB.db.JsonDB._dump_file')
    f = tmpdir.join("test.json")
    db = JsonDB(f.strpath)

    result = db.add_new_key("age")

    assert result is True
