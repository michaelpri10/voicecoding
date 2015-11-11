def verify(val_type, val):
    if val_type in data_types:
        return data_types[val_type](val)
    else:
        return False

def check_int(val):
    try:
        int_val = int(val)
        return int_val
    except ValueError:
        return False

data_types = {
             "integer": check_int
             }
