import pytest
from voicecoding.eval_command import eval_command
from voicecoding.data_types import format_value


@pytest.mark.parametrize(
    "command, expected", [
        ("string hello world", '"hello world"'),
        ("hello world", '"hello world"'),
        ("integer 10", "10"),
        ("10", "10"),
        ("ten", "10"),
        ("float one point two", "1.2"),
        ("float 1 point 2", "1.2"),
        ("one point two", "1.2"),
        ("1.256", "1.256"),
        ("one point 102", "1.102"),
        ("boolean true", "True"),
        ("false", "False"),
        ("variable x", "x"),
        ("X", "x"),
        ("equation ten plus 45", "(10+45)"),
        ("equation 3 to the power of four", "(3**4)"),
        ("equation 6 x 12", "(6*12)"),
        ("equation variable X x 4", "(x*4)"),
        ("comparison 10 is greater than 4", "10 > 4"),
        ("comparison 10 is less than or equal to 4 and x is equal to 5",
            "10 <= 4 and x == 5"),
        ("comparison 12 in list 4 cut 8 cut 12", "12 in [4, 8, 12]"),
        ("list", "[]"),
        ("list one cut two cut three", "[1, 2, 3]"),
        ("tuple", "()"),
        ("tuple one", "(1,)"),
        ("tuple one cut x", "(1, x)"),
        ("set", "set()"),
        ("set one cut two cut x", "{1, 2, x}"),
        ("function string params x", "str(x)"),
    ]
)
def test_data_types(command, expected):
    eval_command("assign 10 to variable x")
    assert expected == format_value(command)
