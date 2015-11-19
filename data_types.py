from command_functions.helpers.format_var_func_name import format_var_func_name

def verify(val_type, val):
    if val_type in data_types:
        return data_types[val_type](val)
    else:
        return False

def check_int(val):
    val = val.replace("negative ", "-")
    try:
        int_val = int(val)
        return int_val
    except ValueError:
        return False

def check_str(val):
    return '"{0}"'.format(val)

def check_var(val):
    variable = format_var_func_name(val)
    if not variable:
        return False
    else:
        return variable

data_types = {
             "integer": check_int,
             "string": check_str,
             "variable": check_var
             }
