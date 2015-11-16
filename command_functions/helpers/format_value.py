from data_types import verify

def format_value(val):
    data_type = val.split()[0]
    data_value = " ".join(val.split()[1:])
    var_val = verify(data_type, data_value)
    if var_val:
        return var_val
    else:
        return False
