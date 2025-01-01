import json
from copy import deepcopy

import pytest

from seJsonDB.db import JsonDB
from seJsonDB.errors import SchemaTypeError, SchemaError, IdAllReadyExistError
from seJsonDB.errors import UnknownKeyError


TEST_DATA = {
    'keys': ['age', 'name'],
    'data': {
        '2352346': {
            'age': 4,
            'name': 'mathew'
        }
    }
}


def test_add_empty_file(tmpdir, mocker):
    mocker.patch('seJsonDB.db.JsonDB._gen_id', return_value='2352346')
    f = tmpdir.join('test.json')
    db = JsonDB(f.strpath)

    assert db.add({'age': 4, 'name': 'mathew'}) == '2352346'
    assert json.loads(f.read()) == TEST_DATA


def test_add_non_empty_file(tmpdir, mocker):
    final_data = {
        'keys': ['age', 'name'],
        'data': {
            '2352346': {
                'age': 4,
                'name': 'mathew'
            },
            '1234567': {
                'age': 18,
                'name': 'ad'
            }
        }
    }

    mocker.patch('seJsonDB.db.JsonDB._gen_id', return_value='1234567')
    f = tmpdir.join('test.json')
    f.write(json.dumps(TEST_DATA, indent=4))

    db = JsonDB(f.strpath)
    assert db.add({'name': 'ad', 'age': 18}) == '1234567'
    assert json.loads(f.read()) == final_data


def test_add_unknown_key_error(tmpdir):
    f = tmpdir.join('test.json')
    f.write(json.dumps(TEST_DATA))

    db = JsonDB(f.strpath)
    with pytest.raises(SchemaError):
        db.add({'age': 4, 'name': 'fredy', 'place': 'GB'})


def test_schema_type_error(tmpdir):
    new_test_data = deepcopy(TEST_DATA)
    new_test_data['keys'] = 'test'

    f = tmpdir.join('test.json')
    f.write(json.dumps(new_test_data, indent=4))
    db = JsonDB(f.strpath)
    with pytest.raises(SchemaTypeError):
        db.add({'name': 'test', 'age': 69})


def test_add_keys_mismatched_length(tmpdir):
    f = tmpdir.join('test.json')
    f.write(json.dumps(TEST_DATA))

    db = JsonDB(f.strpath)
    with pytest.raises(SchemaError):
        db.add({'name': 'test'})


@pytest.mark.parametrize(
    'data',
    (
        [0, 2],
        1,
        'hello',
        (1, 2),
        type('Foo', (), {})
    )
)
def test_add_type_error(tmpdir, data):
    f = tmpdir.join('test.json')
    db = JsonDB(f.strpath)
    with pytest.raises(TypeError):
        db.add(data)


def test_add_key_in_data(tmpdir):
    f = tmpdir.join('test.json')
    db = JsonDB(f.strpath)

    assert db.add({'key': 'john', 'name': 'john', 'age': 34, 'knows_python': True}) == 'john'


def test_add_key_in_data_uid(tmpdir, mocker):
    mocker.patch('seJsonDB.db.JsonDB._gen_id', return_value='510fff25-e430-48ac-9f13-5e91a13ebb6a')
    f = tmpdir.join('test.json')
    db = JsonDB(f.strpath)

    assert db.add({'Key': '00000000-0000-0000-0000-000000000000', 'name': 'john', 'age': 34, 'knows_python': True}) == '510fff25-e430-48ac-9f13-5e91a13ebb6a'

    with pytest.raises(IdAllReadyExistError):
        db.add({'Key': '00000000-0000-0000-0000-000000000000', 'name': 'john', 'age': 34, 'knows_python': True})
