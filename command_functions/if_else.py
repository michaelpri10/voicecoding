from data_types import format_value
from code_class import Code


def if_else(to_parse):
    Code.if_else = True
    Code.multiline = True
    if type(Code.code) != dict:
        Code.code = {}
    if to_parse == "else command":
        Code.code[len(Code.code)] = "else:"
    elif to_parse.startswith("elif"):
        if to_parse == "elif":
            return False 
        else:
            Code.code[len(Code.code)] = "elif {0}:".format(format_value(to_parse[4:]))
    else:
        Code.code[0] = "if {0}:".format(format_value(to_parse))
    return
