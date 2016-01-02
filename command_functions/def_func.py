from data_types import format_value
from code_class import Code


def def_func(to_parse):
    Code.multiline = True
    Code.def_func = True
    if type(Code.code) != dict:
        Code.code = {}
    # creates implied comparison
    if to_parse.startswith("function"):
        function = format_value(to_parse)
    else:
        function = format_value("function {0}".format(to_parse))
    if function is False:
        return False
    if len(Code.code) > 0:
        Code.amount_nested += "    "
        Code.code[len(Code.code)] = "{0}def {1}:".format(
            Code.amount_nested, function 
        )
    else:
        Code.code[len(Code.code)] = "def {0}:".format(function)
