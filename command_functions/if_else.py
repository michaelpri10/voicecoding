from data_types import format_value
from code_class import Code


def if_else(to_parse):
    Code.if_else = True
    Code.multiline = True
    if type(Code.code) != dict:
        Code.code = {}
    if to_parse == "else command":
        Code.code[len(Code.code)] = "{0}else:".format(Code.amount_nested)
    elif to_parse.startswith("elif"):
        comparison = format_value(to_parse[4:])
        if to_parse == "elif" or comparison is False:
            return False
        else:
            Code.code[len(Code.code)] = "{0}elif {1}:".format(
                Code.amount_nested, comparison
            )
    else:
        comparison = format_value(to_parse)
        if comparison is False:
            return False
        if len(Code.code) > 0:
            Code.amount_nested += "    "
            Code.code[len(Code.code)] = "{0}if {1}:".format(
                Code.amount_nested, comparison
            )
        else:
            Code.code[len(Code.code)] = "if {0}:".format(comparison)
    return
