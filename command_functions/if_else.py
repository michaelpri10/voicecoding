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
        if to_parse == "elif":
            return False 
        else:
            Code.code[len(Code.code)] = "{0}elif {1}:".format(Code.amount_nested, format_value(to_parse[4:]))
    else:
        if len(Code.code) > 0:
            Code.amount_nested += "    "
            Code.code[len(Code.code)] = "{0}if {1}:".format(Code.amount_nested, format_value(to_parse))
        else:
            Code.code[0] = "if {0}:".format(format_value(to_parse))
    print(Code.code)
    return
