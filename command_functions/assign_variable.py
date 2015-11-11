from data_types import verify

def assign_variable(to_parse):
    unformatted_name_place = to_parse.find(" to variable ")
    if unformatted_name_place == -1:
        return False
    unformatted_name = to_parse[unformatted_name_place+13:]
    print("name: ", unformatted_name)
    unparsed_value = to_parse[:unformatted_name_place]
    print("value: ", unparsed_value)

    var_name = format_var_name(unformatted_name)
    print(var_name)

    var_value = format_value(unparsed_value)
    print(var_value)

    if not var_name or not var_value:
        return False
    else:
        return "{0} = {1}".format(var_name, var_value)


def format_var_name(name):
    lowercased_name = name.lower()
    snaked_name = lowercased_name.replace(" ", "_")
    return snaked_name

def format_value(val):
    print(val.split())
    data_type = val.split()[0]
    data_value = " ".join(val.split()[1:])
    var_val = verify(data_type, data_value)
    if var_val:
        return var_val
    else:
        return False
