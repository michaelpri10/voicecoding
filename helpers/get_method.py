from helpers.to_builtin import to_builtin 
from helpers.voice_conversion import voice_conversion 
from helpers.get_params import get_params 
from helpers.format_var_func_name import format_var_func_name

def get_method(val):
    val = voice_conversion(val, "method")
    print(val)
    if "method" in val: 
        method_spot = val.find("method") 
        parameters = get_params(val)
        print(parameters)
        method = val.split("parameters")[0][method_spot+7:]
        if to_builtin(method):
            method = to_builtin(method)
        else:
            method = format_var_func_name(method)
        if parameters == False:
            return False
        else:
            return [".{0}{1}".format(method, parameters), val[method_spot:]]
    else:
        return ["", ""]
