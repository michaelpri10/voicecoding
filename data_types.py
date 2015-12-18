from command_functions.helpers.format_var_func_name import format_var_func_name
from text2num import text2num

def verify(val, val_type=None):
    if val_type == None:
        for i in assumed_data_types:
            if i(val) == False:
                pass 
            else:
                return i(val)
    if val_type in data_types:
        return data_types[val_type](val)
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

def check_str(val):
    return '"{0}"'.format(val)

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
    print(equation)
    
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

def check_bool(val):
    if val.lower() == "false":
        return "False"
    elif val.lower() in ["true", "through", "tru"]:
        return "True"
    else:
        return False

def check_list(val):
    list_items = val.split("cut")
    formatted = [format_value(i) for i in list_items]
    for i in formatted:
        if type(i) is str:
            formatted[formatted.index(i)] = i.replace('"', "")
    if False in formatted:
        return False
    else:
        for i in formatted:
            if str(i).lower() == "false":
                formatted[formatted.index(i)] = False
            elif str(i).lower() in ["true", "through", "tru"]:
                formatted[formatted.index(i)] = True
        return "{0}".format(formatted)

assumed_data_types = [check_int,  check_bool, check_str]

data_types = {
             "string": check_str,
             "integer": check_int,
             "boolean": check_bool,
             "variable": check_var,
             "equation": check_equation,
             "list": check_list
             }
