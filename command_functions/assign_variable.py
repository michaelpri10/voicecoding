from helpers.format_var_func_name import format_var_func_name
from data_types import format_value

def assign_variable(to_parse):
    v = "to variable"
    to_parse = to_parse.replace("the variable", v)
    to_parse = to_parse.replace("two variable", v) 
    to_parse = to_parse.replace("- variable ", v) 
    unformatted_name_place = to_parse.find(" to variable ")
    if unformatted_name_place == -1:
        return False
    unformatted_name = to_parse[unformatted_name_place+13:]
    unparsed_value = to_parse[:unformatted_name_place]

    var_name = format_var_func_name(unformatted_name)
    var_value = format_value(unparsed_value)

    if not var_name or not var_value:
        return False
    else:
        return "{0} = {1}".format(var_name, var_value)


