from data_types import format_value
from helpers.format_var_func_name import format_var_func_name
from code_class import Code


def for_loop(to_parse):
    if " in " not in to_parse:
        return False
    else:
        Code.for_loop = True
        Code.multiline = True
        if type(Code.code) != dict:
            Code.code = {}
        parts = to_parse.split(" in ")
        variable = format_var_func_name(parts[0])
        iterable = format_value(parts[1])
        if len(Code.code) > 0:
            Code.amount_nested += "    "
            Code.code[len(Code.code)] = "{0}for {1} in {2}:".format(
                Code.amount_nested, variable, iterable
            )
        else:
            Code.code[len(Code.code)] = "for {0} in {1}:".format(
                variable, iterable
            )
