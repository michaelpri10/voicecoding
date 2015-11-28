from command_functions.helpers.format_var_func_name import format_var_func_name

def verify(val_type, val):
    if val_type in data_types:
        return data_types[val_type](val)
    else:
        return False

def format_value(val):
    data_type = val.split()[0]
    data_value = " ".join(val.split()[1:])
    var_val = verify(data_type, data_value)
    if var_val:
        return var_val
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

def check_equation(val):
    operations = {"plus": "+",
                  "+ ": " + ",
                  "minus": "-",
                  "times": "*",
                  "X integer": " * integer",
                  "X variable": " * variable",
                  "x integer": " * integer",
                  "x variable": " * variable",
                  "divided by": "/",
                  "over": "/",
                  "to the power of": "**"
                 }
    equation = val
    for i in operations:
        equation = equation.replace(i, operations[i])
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

data_types = {
             "integer": check_int,
             "string": check_str,
             "strength": check_str,
             "variable": check_var,
             "equation": check_equation
             }
