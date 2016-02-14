from ..code_class import Code


# imports a module so it can be utilized
def import_module(to_parse):
    # formats module name
    module = to_parse.replace(" ", "")

    # add module to defined vars so it doesn't have to be specified
    Code.defined_vars.add(module)
    return "import {0}".format(module)
