# seJsonDB
A Simple, Lightweight, Efficient JSON based database for Python.
 
 ***

### Installation

To install `seJsonDB`, use pip:

 ```bash
   pip install seJsonDB
 ```
## Features

* __Lightweight__ JSON based database.
* Supports __CRUD__ commands.
* No Database drivers required.
* __Unique ID__ assigned for each JSON document added.
* Strict about __Schema__ of data added. 

```python
>> from seJsonDB import JsonDB
>> db = JsonDB("test.json")
>> db.add_many([{"key": "jsondb", "name":"jsondb","type":"DB"},{"key": "jsondb3","name":"pysondb3","type":"DB"}])
    ({}, {0: {'Exception': 'Id `jsondb` already in DB', 'data': {'key': 'jsondb', 'name': 'jsondb', 'type': 'DB'}}, 1: {'Exception': 'Id `jsondb3` already in DB', 'data': {'key': 'jsondb3', 'name': 'pysondb3', 'type': 'DB'}}})
>> db.get_all()
    {'jsondb': {'key': 'jsondb', 'name': 'jsondb', 'type': 'DB'}, 'jsondb3': {'key': 'jsondb3', 'name': 'pysondb3', 'type': 'DB'}}
```
* See its simple....


## Quick walk through of all the methods

_Coming Soon_
