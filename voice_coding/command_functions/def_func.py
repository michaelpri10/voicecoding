from ..data_types import format_value
from ..code_class import Code
from ..helpers.voice_conversion import voice_conversion


# defines a function
def def_func(to_parse):
    Code.multiline = True
    Code.def_func = True
    if type(Code.code) != dict:
        Code.code = {}
    to_parse = voice_conversion(to_parse, "function")

    if len(to_parse.split("parameters")) > 1:
        param_items = to_parse.split("parameters")[-1].split("cut")
        for i in range(len(param_items)):
            if param_items[i].lstrip().startswith("variable"):
                param_items[i] = param_items[i].lstrip()
            else:
                param_items[i] = "variable {0}".format(param_items[i].lstrip())
        to_parse = "{0} parameters {1}".format(
            to_parse.split("parameters")[0], " cut ".join(param_items)
        )

    # creates implied function data type
    if to_parse.startswith("function"):
        function = format_value(to_parse)
    else:
        function = format_value("function {0}".format(to_parse))
    if function is False:
        return False
    # add function parameters to defined_vars
    parameters = function[function.find("(")+1:function.find(")")].split(",")
    for i in parameters:
        Code.defined_vars.add(i)
        Code.loop_func_vars.append(i)
    # indent if not the first line
    if len(Code.code) > 0:
        Code.amount_nested += "    "
        Code.code[len(Code.code)] = "{0}def {1}:".format(
            Code.amount_nested, function
        )
    else:
        Code.code[len(Code.code)] = "def {0}:".format(function)
