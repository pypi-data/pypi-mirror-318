from typing import Any
from typing import Callable

from parsimonious import ParseError

from .visitor import Visitor
from .grammar import get_grammar
from py_dictfind.exceptions import PyDictFindInputError


def get_checker(condition: str) -> Callable[[dict[str, Any]], bool]:
    """Returns a function that takes a dictionary and returns if it matches `condition`."""

    # get grammar tree
    grammar = get_grammar()
    try:
        tree = grammar.parse(condition)
    except ParseError as err:
        raise PyDictFindInputError(f"Condition '{condition}' can't be parsed: {err}.")

    # get associated visitor
    visitor = Visitor()
    checker = visitor.visit(tree)

    return checker
