from data_types import format_value


def print_data(to_parse):
    print_value = format_value(to_parse)
    if print_value is False:
        return False
    else:
        return "print({0})".format(print_value)
