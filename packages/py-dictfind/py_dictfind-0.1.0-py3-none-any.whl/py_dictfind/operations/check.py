from typing import Any

from py_dictfind.models import get_checker


def check(data: dict[str, Any], condition: str) -> bool:
    """Check if the provided dictionary meets the provided condition."""

    checker = get_checker(condition)
    result = checker(data)

    return result
