from helpers.convert_list_vals import convert_list_vals


# returns the parameters for a function or method
def get_params(val):
    if len(val.split("parameters")) > 1:
        param_items = val.split("parameters")[-1].split("cut")
        parameters = convert_list_vals(param_items)
    else:
        parameters = ""
    if parameters is False:
        return False
    else:
        parameters = "{0}{1}{2}".format("(", parameters[1:-1], ")")
    return parameters
