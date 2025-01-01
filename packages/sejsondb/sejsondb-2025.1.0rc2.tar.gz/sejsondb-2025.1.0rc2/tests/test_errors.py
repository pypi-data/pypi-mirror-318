from seJsonDB.errors import BaseCustomError
from seJsonDB.errors import SchemaTypeError
from seJsonDB.errors import IdDoesNotExistError
from seJsonDB.errors import IdAllReadyExistError
from seJsonDB.errors import SchemaError
from seJsonDB.errors import SchemaKeyError


def test_base_custom_error_initialization():
    error_message = "A base custom error occurred."
    error = BaseCustomError(error_message)
    assert str(error) == error_message


def test_schema_type_error_initialization():
    error_message = "Invalid schema type provided."
    error = SchemaTypeError(error_message)
    assert str(error) == error_message


def test_schema_type_error_is_instance_of_base_custom_error():
    error = SchemaTypeError("Test message")
    assert isinstance(error, SchemaTypeError)


def test_id_does_not_exist_error_inherits_base_custom_error():
    error_message = "The requested ID does not exist."
    error = IdDoesNotExistError(error_message)
    assert isinstance(error, IdDoesNotExistError)
    assert str(error) == error_message


def test_id_does_not_exist_error_with_empty_message():
    error_message = ""
    error = IdDoesNotExistError(error_message)
    assert isinstance(error, IdDoesNotExistError)
    assert str(error) == error_message


def test_id_does_not_exist_error_with_special_characters():
    error_message = "ID not found! @#$%^&*()"
    error = IdDoesNotExistError(error_message)
    assert isinstance(error, IdDoesNotExistError)
    assert str(error) == error_message


def test_id_does_not_exist_error_with_long_message():
    error_message = "X" * 1000  # Long message of 1000 characters
    error = IdDoesNotExistError(error_message)
    assert isinstance(error, IdDoesNotExistError)
    assert str(error) == error_message


def test_id_already_exist_error_initialization():
    error_message = "An ID already exists in the system."
    error = IdAllReadyExistError(error_message)
    assert str(error) == error_message


def test_id_already_exist_error_inheritance():
    error = IdAllReadyExistError("Error message")
    assert isinstance(error, Exception)


def test_schema_error_initialization():
    error_message = "A schema error occurred."
    error = SchemaError(error_message)
    assert str(error) == error_message


def test_schema_error_inheritance():
    error = SchemaError("Testing inheritance.")
    assert isinstance(error, Exception)
    assert isinstance(error, SchemaError)


def test_schema_key_error_initialization():
    error_message = "A schema key error occurred."
    error = SchemaKeyError(error_message)
    assert str(error) == error_message