from ..data_types import format_value
from ..code_class import Code


def while_loop(to_parse):
    Code.if_else_loop = True
    Code.multiline = True
    if type(Code.code) != dict:
        Code.code = {}
    # creates implied comparison
    if to_parse.startswith("comparison"):
        comparison = format_value(to_parse)
    else:
        comparison = format_value("comparison {0}".format(to_parse))
    if comparison is False:
        return False
    # indents code if not the first line in the loop
    if len(Code.code) > 0:
        Code.amount_nested += "    "
        Code.code[len(Code.code)] = "{0}while {1}:".format(
            Code.amount_nested, comparison
        )
    else:
        Code.code[len(Code.code)] = "while {0}:".format(comparison)
