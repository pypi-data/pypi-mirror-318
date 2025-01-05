import re
from math import isclose

from parsimonious.nodes import NodeVisitor

from py_dictfind.logs import log


class Visitor(NodeVisitor):
    # expressions

    def visit_expr(self, node, visited_children):
        log.debug(f"--\nexpr: {node.text}")
        head, tail = visited_children
        funcs = [head] + tail
        return lambda data: any([func(data) for func in funcs])

    def visit_or_many(self, node, visited_children):
        return visited_children

    def visit_or_partial(self, node, visited_children):
        _, _, _, func = visited_children
        return func

    def visit_and_expr(self, node, visited_children):
        head, tail = visited_children
        funcs = [head] + tail
        return lambda data: all([func(data) for func in funcs])

    def visit_and_many(self, node, visited_children):
        return visited_children

    def visit_and_partial(self, node, visited_children):
        _, _, _, func = visited_children
        return func

    def visit_not_expr(self, node, visited_children):
        return visited_children[0]

    def visit_not_partial_expr(self, node, visited_children):
        _, _, func = visited_children
        return lambda data: not func(data)

    def visit_not_condition(self, node, visited_children):
        _, _, func = visited_children
        return lambda data: not func(data)

    def visit_partial_expr(self, node, visited_children):
        _, _, expr, _, _ = visited_children
        return expr

    # conditions

    def visit_condition(self, node, visited_children):
        log.debug(f"condition: {node.text}")
        return visited_children[0]

    def visit_existence(self, node, visited_children):
        log.debug(f"existence: {node.text}")

        def convert_to_bool_factory(ref_func):
            def convert_to_bool(data):
                try:
                    _ = ref_func(data)
                except Exception:
                    return False
                return True

            return convert_to_bool

        ref_func = visited_children[0]
        return convert_to_bool_factory(ref_func)

    def visit_comparison(self, node, visited_children):
        log.debug(f"comparison: {node.text}")

        def convert_to_bool_factory(comparison_func):
            def convert_to_bool(data):
                try:
                    result = comparison_func(data)
                except (KeyError, IndexError):
                    return False
                return bool(result)

            return convert_to_bool

        comparison_func = visited_children[0]
        return convert_to_bool_factory(comparison_func)

    def visit_ref_comparison(self, node, visited_children):
        ref1, _, op, _, ref2 = visited_children
        return lambda data: op(ref1(data), ref2(data))

    def visit_lit_comparison(self, node, visited_children):
        ref, _, op, _, literal = visited_children
        return lambda data: op(ref(data), literal)

    def visit_op(self, node, visited_children):
        return visited_children[0]

    def visit_eq(self, node, visited_children):
        def check_eq(val1, val2):
            if isinstance(val2, float):
                return isclose(val1, val2)
            else:
                return val1 == val2

        return check_eq

    def visit_ne(self, node, visited_children):
        return lambda val1, val2: val1 != val2

    def visit_re(self, node, visited_children):
        def check_regex(val1, val2):
            try:
                result = re.match(val2, val1)
            except TypeError:
                raise ValueError(
                    "The ~= operator requires both the key value and the pattern to be strings. "
                    f" Value: '{val1}'. Pattern: '{val2}'."
                )
            return bool(result)

        return check_regex

    def visit_lt(self, node, visited_children):
        return lambda val1, val2: val1 < val2

    def visit_gt(self, node, visited_children):
        return lambda val1, val2: val1 > val2

    def visit_lte(self, node, visited_children):
        return lambda val1, val2: val1 <= val2

    def visit_gte(self, node, visited_children):
        return lambda val1, val2: val1 >= val2

    # refs

    def visit_ref(self, node, visited_children):
        log.debug(f"ref: {node.text}")

        def lookup_function_factory(keys):
            def lookup_function(data):
                container = data
                for key in keys:
                    if isinstance(container, list) or isinstance(container, tuple):
                        container = container[int(key)]
                    else:
                        container = container[key]
                element = container
                return element

            return lookup_function

        _, head_id, other_ids = visited_children
        all_ids = [head_id] + other_ids
        return lookup_function_factory(all_ids)

    def visit_access_many(self, node, visited_children):
        return visited_children

    def visit_dot_access(self, node, visited_children):
        _, bare_id = visited_children
        return bare_id

    # ids

    def visit_simple_id(self, node, visited_children):
        log.debug(f"simple_id: {node.text}")
        return visited_children[0]

    def visit_bare_id(self, node, visited_children):
        return node.text

    def visit_quoted_id(self, node, visited_children):
        _, text, _ = visited_children
        return text

    def visit_quoted_id_inner(self, node, visited_children):
        return node.text

    def visit_bracket_id(self, node, visited_children):
        _, text, _ = visited_children
        return text

    def visit_bracket_id_inner(self, node, visited_children):
        return node.text

    # literals

    def visit_literal(self, node, visited_children):
        log.debug(f"literal: {node.text}")
        return visited_children[0]

    def visit_string(self, node, visited_children):
        return visited_children[0]

    def visit_squote_string(self, node, visited_children):
        _, text, _ = visited_children
        return text

    def visit_squote_string_inner(self, node, visited_children):
        escaped_string = "".join(visited_children)
        actual_string = escaped_string.replace(r"\'", "'").replace(r"\"", '"')
        log.debug(f"squote visited_children: {visited_children}")
        log.debug(f"squote escaped_string: {escaped_string}")
        log.debug(f"squote actual_string: {actual_string}")
        log.debug(f"squote equal: {actual_string == escaped_string}")
        return actual_string

    def visit_squote_string_inner_parts(self, node, visited_children):
        return node.text

    def visit_dquote_string(self, node, visited_children):
        _, text, _ = visited_children
        return text

    def visit_dquote_string_inner(self, node, visited_children):
        escaped_string = "".join(visited_children)
        actual_string = escaped_string.replace(r"\'", "'").replace(r"\"", '"')
        return actual_string

    def visit_dquote_string_inner_parts(self, node, visited_children):
        return node.text

    def visit_escape(self, node, visited_children):
        return node.text

    def visit_bool(self, node, visited_children):
        return node.text.lower() == "true"

    def visit_float(self, node, visited_children):
        return float(node.text)

    def visit_int(self, node, visited_children):
        return int(node.text)

    def generic_visit(self, node, visited_children):
        pass
