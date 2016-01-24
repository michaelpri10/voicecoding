from ..data_types import format_value


# calls a function or method
def call_func_method(to_parse):
    # makes sure the command is a function or method
    if to_parse.startswith("function") or to_parse.find("method") != -1:
        to_call = format_value(to_parse)
        if to_call is False:
            return False
        else:
            return "{0}".format(to_call)
    else:
        return False
