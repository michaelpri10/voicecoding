from command_functions.assign_variable import assign_variable
from command_functions.print_data import print_data
from command_functions.call_func_method import call_func_method
from command_functions.if_else import if_else

# commands that can be called by the user; the first word in the voice command
instructions = {"assign": assign_variable,
                "print": print_data,
                "call": call_func_method,
                "if": if_else}
