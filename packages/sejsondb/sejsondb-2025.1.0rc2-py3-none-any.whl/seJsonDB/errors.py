class BaseCustomError(Exception):
    """Base class for custom exceptions to reduce redundancy."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class SchemaTypeError(BaseCustomError):
    """Exception raised for schema type errors."""
    pass


class IdDoesNotExistError(BaseCustomError):
    """Exception raised for ID does not exist errors."""
    pass


class IdAllReadyExistError(BaseCustomError):
    """Exception raised for ID already exist errors."""
    pass


class SchemaError(BaseCustomError):
    """Exception raised for general schema-related errors."""
    pass


class SchemaKeyError(BaseCustomError):
    """Exception raised for schema key errors."""
    pass

class UnknownKeyError(BaseCustomError):
    """
    Represents an error raised when a specified key is not found or is invalid.

    This exception is specifically used to signal the absence of a required key
    or the use of an invalid key in operations where such keys are expected. It
    serves as a more descriptive alternative to generic exceptions (like KeyError)
    for cases involving unknown keys.
    """
    pass