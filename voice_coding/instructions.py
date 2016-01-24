from .assign_variable import assign_variable
from .print_data import print_data
from .call_func_method import call_func_method
from .if_else import if_else
from .for_loop import for_loop
from .while_loop import while_loop
from .def_func import def_func
from .return_func import return_func

# commands that can be called by the user; the first word in the voice command
instructions = {"assign": assign_variable,
                "print": print_data,
                "call": call_func_method,
                "if": if_else,
                "for": for_loop,
                "while": while_loop,
                "define": def_func,
                "return": return_func}
