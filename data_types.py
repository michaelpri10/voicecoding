from helpers.format_var_func_name import format_var_func_name
from helpers.text2num import text2num
from helpers.convert_list_vals import convert_list_vals
from helpers.to_builtin import to_builtin
from helpers.voice_conversion import voice_conversion
from helpers.get_method import get_method
from helpers.get_params import get_params

def verify(val, val_type=None):
    method = get_method(val)
    val = voice_conversion(val, "method").replace(method[1], "").rstrip()
    if val_type == None:
        for i in assumed_data_types:
            if i(val) == False:
                pass 
            else:
                return "{0}{1}".format(i(val), method[0])
    if val_type in data_types:
        return "{0}{1}".format(data_types[val_type](val), method[0])
    else:
        return False

def format_value(val):
    val = val.strip()
    try:
        data_type = val.split()[0].lower()
    except:
        data_type = None
    if data_type in data_types:
        data_value = " ".join(val.split()[1:])
        var_val = verify(data_value, data_type)
    else:
        var_val = verify(val)
    if var_val == False:
        return False
    else:
        return var_val

def check_str(val):
    if val == "space":
        val = " "
    return '"{0}"'.format(val)

def check_int(val):
    try:
        val = text2num(val)
    except:
        pass
    try:
        int_val = int(val)
        return int_val
    except ValueError:
        return False

def check_float(val):
    val = val.replace("point", ".")
    parts = val.split(".")
    try:
        parts[0] = str(text2num(parts[0]))
        parts[1] = str(text2num(parts[1]))
    except:
        pass
    try:
        val_float = float(".".join(parts))
        return val_float
    except:
        return False

def check_bool(val):
    if val.lower() == "false":
        return "False"
    elif val.lower() in ["true", "through", "tru"]:
        return "True"
    else:
        return False

def check_var(val):
    variable = format_var_func_name(val)
    if not variable:
        return False
    else:
        return variable

def check_equation(val):
    operations = {"plus": "+",
                  "Plus": "+",
                  "+ ": " + ",
                  "minus": "-",
                  "times": "*",
                  "divided by": "/",
                  "over": "/",
                  "to the power of": "**"
                 }
    equation = val
    for i in operations:
        equation = equation.replace(i, operations[i])
    if "variable X" not in equation and "variable x" not in equation:
        equation = equation.replace(" x ", " * ")
        equation = equation.replace(" X ", " * ")
    
    eq_operations = [i for i in equation.split() if i in operations.values()]
    if len(eq_operations) == 0:
        return False

    operands = equation 
    for i in eq_operations:
        operands = operands.replace(i, "(@!@)")

    operand_dict = {}
    for i in operands.split("(@!@)"):
        operand_dict[i] = format_value(i)

    if False in operand_dict.values():
        return False

    for i in operand_dict:
        equation = equation.replace(i, str(operand_dict[i]))
    
    return "({0})".format(equation)

def check_list(val):
    list_items = val.split("cut")
    l = convert_list_vals(list_items)
    if l == False:
        return False
    else:
        return "{0}".format(l)

def check_tuple(val):
    tuple_items = val.split("cut")
    t = convert_list_vals(tuple_items)
    if t == False:
        return False
    else:
        if t == []:
            return "()"
        elif "," not in t:
            return "{0}{1}{2}".format("(", t[1:-1], ",)")
        else:
            return "{0}{1}{2}".format("(", t[1:-1], ")")

def check_set(val):
    set_items = val.split("cut")
    s = convert_list_vals(set_items)
    if s == False:
        return False
    else:
        if s == []:
            return "set()"
        else:
            return "{0}{1}{2}".format("{", s[1:-1], "}")

def check_func(val):
    val = voice_conversion(val, "function") 
    parameters = get_params(val)
    function_name = val.split("parameters")[0]
    if to_builtin(function_name):
        function_name = to_builtin(function_name)
    else:
        function_name = format_var_func_name(function_name.rstrip())
    if parameters == False:
        return False
    else:
        return "{0}{1}".format(function_name, parameters)
    
assumed_data_types = [check_int, check_float, check_bool, check_str]

data_types = {
             "string": check_str,
             "integer": check_int,
             "float": check_float,
             "boolean": check_bool,
             "variable": check_var,
             "equation": check_equation,
             "list": check_list,
             "tuple": check_tuple,
             "set": check_set,
             "function": check_func
             }
