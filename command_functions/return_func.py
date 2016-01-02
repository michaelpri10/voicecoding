from data_types import format_value
from code_class import Code


def return_func(to_parse):
    if Code.def_func is False:
        return False
    else:
        to_return = format_value(to_parse)
        if to_return is False:
            return False
        else:
            return "return {0}".format(to_return)
