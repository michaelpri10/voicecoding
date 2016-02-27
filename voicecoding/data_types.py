from .helpers.format_var_func_name import format_var_func_name
from .helpers.text2num import text2num
from .helpers.to_builtin import to_builtin
from .helpers.voice_conversion import voice_conversion
from .code_class import Code


# checks and returns the data type
def verify(val, val_type=None):
    # checks if there is a method, returns it, and modifies val
    method = get_method(val)
    val = voice_conversion(val, "method").replace(method[1], "").rstrip()
    # checks for assumed data types (int, float, bool, str) if no data is named
    if val_type is None:
        if check_bool(val) is not False:
            return "{0}".format(check_bool(val))
        else:
            for i in assumed_data_types:
                if i(val) is False:
                    pass
                else:
                    return "{0}{1}".format(i(val), method[0])
    # check for data type if data type is named
    if val_type in data_types:
        if data_types[val_type](val) is False:
            return False
        else:
            return "{0}{1}".format(data_types[val_type](val), method[0])
    else:
        return False


# formats the data type according what type it is; used by the commands
def format_value(val):
    val = val.strip()
    # checks if data type is named
    try:
        data_type = val.split()[0].lower()
        data_type = voice_conversion(val.split()[0].lower(), "data_type")
    except:
        data_type = None
    # verifies a named data type
    if data_type in data_types:
        data_value = " ".join(val.split()[1:])
        var_val = verify(data_value, data_type)
    else:
        var_val = verify(val)
    # checks if a data type was returned
    if var_val is False:
        return False
    else:
        return var_val


# converts a list of values to proper data types
def convert_list_vals(vals):
    # (bug fix) removes first or last item if it is blank
    if vals[0] == '':
        vals.pop(0)
    if len(vals) > 0 and vals[-1] == '':
        vals.pop()
    # return empty list if there or no values in it
    if len(vals) == 0:
            return []
    # formats the values in the list
    formatted = [format_value(i) for i in vals]
    # if any of the data types is False, invalid command
    if False in formatted:
        return False
    else:
        for i in formatted:
            # converts booleans (a bug that fixed a bug)
            if str(i).lower() == "false":
                formatted[formatted.index(i)] = False
            elif str(i).lower() in ["true", "through", "tru"]:
                formatted[formatted.index(i)] = True
        # hack that formats variables and strings properly
        final = "".join([i for i in list(str(formatted)) if i != "'"])

        return final


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


# checks for and returns a method
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


# returns a string
def check_str(val):
    if val == "space":
        val = " "
    return '"{0}"'.format(val)


# returns an integer
def check_int(val):
    # converts words to numbers
    try:
        val = text2num(val)
    except:
        pass
    # checks if val is an integer
    try:
        int_val = int(val)
        return int_val
    except ValueError:
        return False


# returns a float
def check_float(val):
    val = val.replace(" point ", ".")
    parts = val.split(".")
    try:
        # convert whole number words to a number
        parts[0] = str(text2num(parts[0]))
        # convert decimal words to a number
        parts[1] = str(text2num(parts[1]))
    except:
        pass
    try:
        # joins whole number and decimal together
        val_float = float(".".join(parts))
        return val_float
    except:
        return False


# returns a boolean
def check_bool(val):
    if val.lower() == "false":
        return "False"
    elif val.lower() in ["true", "through", "tru"]:
        return "True"
    else:
        return False


# returns a variable
def check_var(val):
    # formats variable name to snake_case
    variable = format_var_func_name(val)
    if not variable:
        return False
    else:
        return variable


# returns a variable; runs when "variable" is not said
def check_var_assumed(val):
    variable = format_var_func_name(val)
    if not variable:
        return False
    else:
        # makes sure variable has been defined already
        if variable not in Code.defined_vars:
            return False
        else:
            return variable


def check_module(val):
    module = val.replace(" ", "")
    if not module:
        return False
    else:
        return module


def check_module_assumed(val):
    module = val.replace(" ", "")
    module = module.replace("-", "")
    if not module:
        return False
    else:
        if module not in Code.defined_vars:
            return False
        else:
            return module


# returns an equation
def check_equation(val):
    # maps words to an operation
    operations = {
        "plus": "+",
        "Plus": "+",
        "+ ": " + ",
        " +": " + ",
        "minus": "-",
        "times": "*",
        "multiplied by": "*",
        "x": "*",
        "divided by": "/",
        "over": "/",
        "to the power of": "**",
        "^": "**",
        "modulus": "%",
        " mod ": " % ",
        "madh": "%",
        "made": "%",
        "iPod": "i %",
        "a modulus": "i %"
    }

    # hacky solution for using variable `x` in an  equation
    val = val.replace("variable X", "this is a variable hack")
    val = val.replace("variable x", "this is a variable hack")
    # replaces words that map to an operation
    for i in operations:
        val = val.replace(i, operations[i])
    val = val.replace("this is a variable hack", "x")
    # keeps track of operations that are being used
    eq_operations = [i for i in val.split() if i in operations.values()]
    if len(eq_operations) == 0:
        return False

    # converts the operands to data types and formats them with the operations
    operands = val
    for i in eq_operations:
        operands = operands.replace(i, "(@!@)")

    operand_dict = {}
    for i in operands.split("(@!@)"):
        operand_dict[i] = format_value(i)

    if False in operand_dict.values():
        return False

    for i in operand_dict:
        val = val.replace(i, str(operand_dict[i]))

    if val is False:
        return False
    else:
        return "({0})".format(val)


# returns a comparison expression
def check_comp(val):
    # maps words to comparisons
    first_comparisons = {
        "is greater than or equal to": ">=",
        "is greater than or equals to": ">=",
        "is less than or equal to": "<=",
        "is less than or equals to": "<="
    }

    second_comparisons = {
        "equals": "==",
        "is equal to": "==",
        "is equals to": "==",
        "does not equal": "!=",
        "does not equals": "!=",
        "is not equal to": "!=",
        "is not equals to": "!=",
        "is greater than": ">",
        "is less than": "<"
    }

    word_comparisons = {
        "and": "and",
        "hand": "and",
        "not": "not",
        "or": "or",
        "is": "is",
        "in": "in"
    }

    # replaces words that map to a comparison
    for i in first_comparisons:
        val = val.replace(i, first_comparisons[i])
    for i in second_comparisons:
        val = val.replace(i, second_comparisons[i])
    for i in word_comparisons:
        val = val.replace(i, word_comparisons[i])
    val = val.replace("equal", "==")

    # keeps track of the comparison operators being used
    comparisons = [">=", "<=", "==", "!=", ">", "<",
                   "and", "not", "or", "is", "in"]
    comp_ops = [i for i in val.split() if i in comparisons]

    # converts the objects being compared to valid data types
    # and formats them with the comparison operators
    to_compare = val
    for i in comp_ops:
        to_compare = to_compare.replace(i, "(@!@)")

    to_compare_dict = {}
    for i in to_compare.split("(@!@)"):
        to_compare_dict[i] = format_value(i)

    if False in to_compare_dict.values():
        return False

    for i in to_compare_dict:
        val = val.replace(i, " {0} ".format(str(to_compare_dict[i])))

    return "{0}".format(val.rstrip().lstrip())


# returns a list
def check_list(val):
    list_items = val.split("cut")
    l = convert_list_vals(list_items)
    if l is False:
        return False
    else:
        return "{0}".format(l)


# returns a tuple
def check_tuple(val):
    tuple_items = val.split("cut")
    t = convert_list_vals(tuple_items)
    if t is False:
        return False
    else:
        if t == []:
            return "()"
        # if there is only one object in the tuple, add a "," at the end
        elif "," not in t:
            return "{0}{1}{2}".format("(", t[1:-1], ",)")
        else:
            return "{0}{1}{2}".format("(", t[1:-1], ")")


# returns a set
def check_set(val):
    set_items = val.split("cut")
    s = convert_list_vals(set_items)
    if s is False:
        return False
    else:
        # if the set it empty return the `set()` function
        if s == []:
            return "set()"
        else:
            return "{0}{1}{2}".format("{", s[1:-1], "}")


# returns a function
def check_func(val):
    val = voice_conversion(val, "function")
    parameters = get_params(val)
    function_name = val.split("parameters")[0]

    # attempts to make function a Python builtin
    if to_builtin(function_name):
        function_name = to_builtin(function_name)
    else:
        # formats the name as snake_case if it is not a builtin
        function_name = format_var_func_name(function_name.rstrip())
    if parameters is False:
        return False
    else:
        return "{0}{1}".format(function_name, parameters)

# data types that don't need to be explicitly named
assumed_data_types = [
    check_var_assumed,
    check_module_assumed,
    check_int,
    check_float,
    check_str
]

# all data types
data_types = {
    "string": check_str,
    "integer": check_int,
    "float": check_float,
    "boolean": check_bool,
    "variable": check_var,
    "module": check_module,
    "equation": check_equation,
    "comparison": check_comp,
    "list": check_list,
    "tuple": check_tuple,
    "set": check_set,
    "function": check_func
}
