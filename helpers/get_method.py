from helpers.to_builtin import to_builtin
from helpers.voice_conversion import voice_conversion
from helpers.get_params import get_params
from helpers.format_var_func_name import format_var_func_name


# checks and returns a method
def get_method(val):
    val = voice_conversion(val, "method")
    # makes sure that command contains a method call
    if "method" in val:
        method_spot = val.find("method")
        parameters = get_params(val)
        # gets method name and converts it to builtin if it can
        method = val.split("parameters")[0][method_spot+7:]
        if to_builtin(method):
            method = to_builtin(method)
        else:
            method = format_var_func_name(method.rstrip())
        if parameters is False:
            return False
        # returns the method and the text that needs to be removed from val
        else:
            return [".{0}{1}".format(method, parameters), val[method_spot:]]
    else:
        return ["", ""]
