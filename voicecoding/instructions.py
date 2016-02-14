from .commandfunctions.assign_variable import assign_variable
from .commandfunctions.print_data import print_data
from .commandfunctions.call_func_method import call_func_method
from .commandfunctions.if_else import if_else
from .commandfunctions.for_loop import for_loop
from .commandfunctions.while_loop import while_loop
from .commandfunctions.def_func import def_func
from .commandfunctions.return_func import return_func
from .commandfunctions.import_module import import_module

# commands that can be called by the user; the first word in the voice command
instructions = {
    "assign": assign_variable,
    "print": print_data,
    "call": call_func_method,
    "if": if_else,
    "for": for_loop,
    "while": while_loop,
    "define": def_func,
    "return": return_func,
    "import": import_module
}
