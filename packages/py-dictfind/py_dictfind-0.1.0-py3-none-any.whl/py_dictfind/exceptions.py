class PyDictFindException(Exception):
    """PyDictFind base exception."""

    pass


class PyDictFindError(PyDictFindException):
    """Base exeption for PyDictFind errors."""

    pass


class PyDictFindInputError(PyDictFindError):
    """Invalid user provided data."""

    pass
