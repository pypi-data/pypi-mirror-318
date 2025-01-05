from py_dictfind import check


def test_key_presence():
    assert check({"foo": 1}, "foo")


def test_no_key_presence():
    assert not check({"foo": 1}, "bar")


def test_literal_string():
    assert check({"foo": "bar"}, "foo == 'bar'")
    assert check({"foo": "bar"}, 'foo == "bar"')


def test_literal_string_escape():
    assert check({"foo": 'a"b'}, r'foo == "a\"b"')
    assert check({"foo": 'a"b'}, 'foo == "a\\"b"')
    assert check({"foo": "a'b"}, r"foo == 'a\'b'")
    assert check({"foo": "a'b"}, "foo == 'a\\'b'")
    assert check({"foo": 'a"b'}, r'foo == "a\"b"')


def test_literal_integer():
    assert check({"foo": 103948}, "foo == 103948")
    assert check({"foo": -103948}, "foo == -103948")


def test_literal_float():
    assert check({"foo": 0.1 + 0.2}, "foo == 0.3")
    assert check({"foo": -0.1 - 0.2}, "foo == -0.3")


def test_literal_bool():
    assert check({"foo": True}, "foo == true")
    assert check({"foo": False}, "foo == false")
    assert not check({"foo": True}, "foo != true")
    assert not check({"foo": False}, "foo != false")
    assert check({"foo": True}, "foo == True")
    assert check({"foo": False}, "foo == False")
    assert check({"foo": True}, "foo == TRUE")
    assert check({"foo": False}, "foo == FALSE")


def test_op_eq():
    assert check({"foo": 1}, "foo == 1")


def test_op_alt_eq():
    assert check({"foo": 1}, "foo: 1")


def test_op_ne():
    assert check({"foo": 1}, "foo != 0")
    assert not check({"foo": 1}, "foo != 1")


def test_op_gt():
    assert check({"foo": 1}, "foo > 0")
    assert not check({"foo": 1}, "foo > 2")


def test_op_lt():
    assert check({"foo": 1}, "foo < 2")
    assert not check({"foo": 1}, "foo < 0")


def test_op_gte():
    assert check({"foo": 1}, "foo <= 1")
    assert check({"foo": 1}, "foo <= 2")
    assert not check({"foo": 1}, "foo <= 0")


def test_op_lte():
    assert check({"foo": 1}, "foo >= 1")
    assert check({"foo": 1}, "foo >= 0")
    assert not check({"foo": 1}, "foo >= 2")


def test_op_re():
    assert check({"foo": "bar"}, "foo ~= 'b.r'")
    assert check({"foo": "bar"}, "foo ~= 'b[abc]r'")
    assert not check({"foo": "bar"}, "foo ~= '^$'")
    assert not check({"foo": "bar"}, "foo ~= 'b[cde]r'")


def test_op_whitespace():
    assert check({"foo": 1}, "foo==1")
    assert check({"foo": 1}, "foo ==1")
    assert check({"foo": 1}, "foo == 1")
    assert check({"foo": 1}, "foo == 1")
    assert check({"foo": 1}, "foo      ==     1")
    assert check({"foo": 1}, "foo \t == \t 1")


def test_not_condition():
    assert check({"foo": 1}, "not foo == 2")
    assert check({"foo": 1}, "not (foo == 2)")
    assert not check({"foo": 1}, "not (foo != 2)")


def test_and_condition():
    assert check({"foo": 1, "bar": 2}, "foo == 1 and bar == 2")
    assert check({"foo": 1, "bar": 2}, "(foo == 1) and (bar == 2)")
    assert check({"foo": 1, "bar": 2}, "( foo == 1 ) and ( bar == 2 )")
    assert not check({"foo": 1, "bar": 2}, "foo == 1 and bar == 3")


def test_or_condition():
    assert check({"foo": 1, "bar": 2}, "foo == 1 or bar == 2")
    assert check({"foo": 1, "bar": 2}, "foo == 1 or bar == 3")
    assert check({"foo": 1, "bar": 2}, "(foo == 1) or (bar == 3)")
    assert check({"foo": 1, "bar": 2}, "( foo == 1 ) or ( bar == 3 )")
    assert not check({"foo": 1, "bar": 2}, "foo == 2 or bar == 3")


def test_dot_notation():
    data = {
        "foo": {
            "bar": {
                "this": 1,
            },
            "baz": {
                "that": 2,
            },
        },
    }
    assert check(data, ".foo.bar")
    assert check(data, "foo.bar")
    assert check(data, "foo.`bar`")
    assert not check(data, "foo.not_a_key")
    assert check(data, "foo.bar.this == 1")
    assert check(data, ".foo.bar.this == 1")
    assert not check(data, "foo.bar.this == 2")
    assert check(data, "foo.baz.that == 2")


def test_backtick_notation():
    data = {
        "%This is a longer key%": {
            "Especial characters ": "ÑñâáéíóúÄäÖöÜüßÇç",
        },
    }
    assert check(data, "`%This is a longer key%`.`Especial characters `")
    assert not check(data, "`%This is a longer key%`.`Especial characters`")
    assert check(
        data, "`%This is a longer key%`.`Especial characters ` == 'ÑñâáéíóúÄäÖöÜüßÇç'"
    )
