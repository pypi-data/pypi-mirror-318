from typing import Any, Callable, Dict, List, Union


DBSchemaType = Dict[str, Union[int, List[str], Dict[str, Any]]]

IdGeneratorType = Callable[[], str]

NewDataType = Dict[str, dict[str, int | str | bool | list[int | str | bool]]]

NewExDataType = Dict[int, dict[str, str | Any]]

NewKeyValidTypes = Union[List, Dict, str, int, bool]

QueryType = Callable[[Dict[str, Any]], bool]

SimpleTypeGroup = Union[int, str, bool]

ReturnWithIdType = Dict[str, Dict[str, SimpleTypeGroup]]

SingleDataType = Dict[str, Union[int, str, bool, List[SimpleTypeGroup]]]

