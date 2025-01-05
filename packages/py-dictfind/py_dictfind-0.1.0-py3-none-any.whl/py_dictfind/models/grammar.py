from functools import lru_cache

from parsimonious.grammar import Grammar


@lru_cache(maxsize=1)
def get_grammar() -> Grammar:
    """Return a dictionary finding grammar object.

    The grammar is provided using a function factory so that it is not parsed
    at import time. The lru_cache is used in this case to make sure that the
    grammar object is stored and reused in successive calls.
    """
    grammar = Grammar(
        r"""
        expr = and_expr or_many
        or_many = or_partial*
        or_partial = ws "or" ws and_expr

        and_expr   = not_expr and_many
        and_many = and_partial*
        and_partial = ws "and" ws not_expr
        not_expr = not_condition / not_partial_expr / condition / partial_expr
        not_partial_expr = "not" ws? partial_expr
        not_condition = "not" ws condition
        partial_expr = "(" ws? expr ws? ")"

        condition =  comparison / existence
        existence = ref / "\uFFFF"
        comparison = lit_comparison / ref_comparison
        lit_comparison = ref ws? op ws? literal
        ref_comparison = ref ws? op ws? ref
        op     = eq / ne / re / lte / gte / lt / gt
        eq     = "==" / ":"
        ne     = "!="
        re     = "~="
        lte    = "<="
        gte    = ">="
        lt     = "<"
        gt     = ">"

        ref = "."? simple_id access_many
        access_many = dot_access*
        dot_access = "." simple_id

        simple_id = bare_id / quoted_id
        bare_id       = ~r"\w+"
        quoted_id       = "`" quoted_id_inner "`"
        quoted_id_inner = ~r"[^`]*"

        literal = string / float / int / bool
        string = squote_string / dquote_string
        squote_string = "'" squote_string_inner "'"
        squote_string_inner = squote_string_inner_parts*
        squote_string_inner_parts = escape / ~r"[^'\\]+"
        dquote_string = '"' dquote_string_inner '"'
        dquote_string_inner = dquote_string_inner_parts*
        dquote_string_inner_parts = escape / ~r'[^"\\]+'
        escape = ~r'\\.'
        bool   = ~r"true"i / ~r"false"i
        float  = ~r"-?[0-9]+\.[0-9]+"
        int    = ~r"-?[0-9]+"

        ws     = ~r"\s+"
        """
    )
    return grammar
