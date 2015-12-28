from data_types import format_value

def call_func_method(to_parse):
    if to_parse.startswith("function") or to_parse.find("method") != -1:
        to_call = format_value(to_parse)
        if to_call == False:
            return False
        else:
            return "{0}".format(to_call)
    else:
        return False
