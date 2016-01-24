from ..data_types import format_value
from ..code_class import Code


def if_else(to_parse):
    Code.if_else_loop = True
    Code.multiline = True
    # if a multiline statement has been started, initialize it
    if type(Code.code) != dict:
        Code.code = {}
    # inputs `else:` if the user said else
    if to_parse == "else command":
        Code.code[len(Code.code)] = "{0}else:".format(Code.amount_nested)
    # creates an elif statement
    elif to_parse.startswith("elif"):
        # implies comparison if it isn't said
        if to_parse.startswith("comparison"):
            comparison = format_value(to_parse[4:])
        else:
            comparison = format_value("comparison {0}".format(to_parse[4:]))
        if to_parse == "elif" or comparison is False:
            return False
        else:
            Code.code[len(Code.code)] = "{0}elif {1}:".format(
                Code.amount_nested, comparison
            )
    else:
        if to_parse.startswith("comparison"):
            comparison = format_value(to_parse)
        else:
            comparison = format_value("comparison {0}".format(to_parse))
        if comparison is False:
            return False
        # increases indentation is another if statement is said
        if len(Code.code) > 0:
            Code.amount_nested += "    "
            Code.code[len(Code.code)] = "{0}if {1}:".format(
                Code.amount_nested, comparison
            )
        else:
            Code.code[len(Code.code)] = "if {0}:".format(comparison)
    return
