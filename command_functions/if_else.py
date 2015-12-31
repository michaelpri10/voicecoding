from data_types import format_value
from code_class import Code


def if_else(to_parse):
    Code.if_else = True
    Code.multiline = True
    if not Code.code:
        Code.code = {}
    line = format_value(to_parse)
    if to_parse == "else command":
        Code.code[len(Code.code)] = "else:"
    else:
        Code.code[0] = "if {0}:".format(line)
    return
