from typing import Any

from py_dictfind.models import get_checker


def find(data: list[dict[str, Any]], condition: str) -> list[dict[str, Any]]:
    """Return the list of dictionaries from `data` that match `condition`."""
    checker = get_checker(condition)
    return [dictionary for dictionary in data if checker(dictionary)]
