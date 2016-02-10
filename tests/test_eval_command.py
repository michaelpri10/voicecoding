import pytest
from voicecoding.eval_command import eval_command
from voicecoding.code_class import Code


@pytest.mark.parametrize(
    "command, expected", [
        ("assign one hundred to variable x", "x = 100"),
        ("call function print params hello world", 'print("hello world")'),
        ("print hello world", 'print("hello world")'),
    ]
)
def test_single_line(command, expected):
    Code.multiline = False
    Code.code = ""
    code = eval_command(command)
    assert code == expected


@pytest.mark.parametrize(
    "command, expected, code_dict", [
        ("define function square root params number",
            "def square_root(number):", {}),
        ("for i in function range params one cut one hundred one",
            "for i in range(1, 101):", {}),
        ("if ten is greater than four", "if 10 > 4:", {}),
        ("elif ten is less than four", "elif 10 < 4:", 
            {0: "if 10 > 4:", 1: "    print(True)"}),
        ("else", "else:", {0: "if 10 > 4:", 1: "    print(True)",
            2: "elif 10 < 4:", 3: "    print(False)"}),
        ("return list one cut two cut three", "    return [1, 2, 3]", {0: "def return_list():"}),
        ("while true", "while True:", {})
    ]
)
def test_multi_line(command, expected, code_dict):
    Code.multiline = True
    Code.code = code_dict
    eval_command(command)
    assert expected in Code.code.values()
