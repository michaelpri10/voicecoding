from ..data_types import format_value


# prints out data; shorter alternative to "call function print parameters ..."
def print_data(to_parse):
    print_value = format_value(to_parse)
    if print_value is False:
        return False
    else:
        return "print({0})".format(print_value)
