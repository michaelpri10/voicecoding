from command_functions.helpers.format_value import format_value

def print_data(to_parse):
    print_value = format_value(to_parse)
    if not print_value:
        return False
    else:
        return "print({0})".format(print_value)
