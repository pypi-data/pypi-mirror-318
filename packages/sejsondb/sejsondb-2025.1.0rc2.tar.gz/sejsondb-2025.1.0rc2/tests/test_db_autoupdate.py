import json
from pathlib import Path

from seJsonDB.db import JsonDB


TEST_FINAL_DATA = {
    'keys': ['age', 'name'],
    'data': {
        '0': {
            'age': 3,
            'name': 'test'
        }
    }
}


def _new_gen_id(n):
    yield str(n)
    yield from _new_gen_id(n + 1)


def test_autoupdate(tmpdir, mocker):
    f = tmpdir.join('test.json')
    _ids = _new_gen_id(0)
    mocker.patch('seJsonDB.db.JsonDB._gen_id', wraps=lambda: next(_ids))
    db = JsonDB(f.strpath, auto_update=False)
    db.add({
        'name': 'test', 'age': 3
    })

    assert db.auto_update is False
    assert db._au_memory == TEST_FINAL_DATA
    assert Path(f.strpath).is_file() is False


def test_autoupdate_force_load(tmpdir, mocker):
    f = tmpdir.join('test.json')
    _ids = _new_gen_id(0)
    mocker.patch('seJsonDB.db.JsonDB._gen_id', wraps=lambda: next(_ids))
    f.write(json.dumps(TEST_FINAL_DATA))
    db = JsonDB(f.strpath, auto_update=False)

    db.force_load()
    assert db.auto_update is False
    assert db._au_memory == TEST_FINAL_DATA


def test_autoupdate_commit(tmpdir, mocker):
    f = tmpdir.join('test.json')
    _ids = _new_gen_id(0)
    mocker.patch('seJsonDB.db.JsonDB._gen_id', wraps=lambda: next(_ids))
    db = JsonDB(f.strpath, auto_update=False)
    db.add({
        'name': 'test', 'age': 3
    })
    db.commit()

    assert db.auto_update is False
    assert json.loads(f.read()) == TEST_FINAL_DATA


def test_autoupdate_accidental_commit(tmpdir):
    f = tmpdir.join('test.json')
    db = JsonDB(f.strpath)
    db.commit()

    assert db.auto_update is True


def test_autoupdate_accidental_force_load(tmpdir):
    f = tmpdir.join('test.json')
    f.write(json.dumps(TEST_FINAL_DATA))

    db = JsonDB(f.strpath)
    db.force_load()

    assert db.auto_update is True