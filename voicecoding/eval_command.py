from .instructions import instructions
from .code_class import Code
from .helpers.voice_conversion import voice_conversion


# evaluates the voice command
def eval_command(command):
    # checks for the instruction
    command = voice_conversion(command, "command")
    instruction = command.split()[0]
    # exits if instruction is "exit"
    if instruction.lower() == "exit":
        print("Exiting...")
        quit()
    # unindent a multiline statement
    if instruction.lower() == "end":
        if Code.multiline:
            Code.code[len(Code.code)] = "{0}end".format(Code.amount_nested)
            Code.amount_nested = Code.amount_nested[:-4]
        return
    # cancel multiline statement
    elif instruction.lower() == "cancel":
        Code.multiline = False
        Code.if_else_loop = False
        Code.code = ""
        Code.amount_nested = ""
        Code.output.append("\n")
        for i in Code.loop_func_vars:
            Code.defined_vars.remove(i)
        Code.loop_func_vars = []
        return

    # if there is nothing after the instruction, invalid command
    if len(command.split()) == 1:
        return False

    # gets and runs voice command that will be used with the instruction
    to_parse = " ".join(command.split()[1:])
    if instruction in instructions:
        # special formatting if currently in a
        # loop/if-else statement/function definition
        if Code.if_else_loop or Code.def_func:
            to_parse = voice_conversion(to_parse, "if-else/loop")
            to_add = instructions[instruction](to_parse)
            if to_add not in [None, False]:
                Code.code[len(Code.code)] = "{0}    {1}".format(
                    Code.amount_nested, to_add
                )
                return
            elif to_add is False:
                Code.errors.append("Invalid command")
                return False
        else:
            return instructions[instruction](to_parse)
    else:
        return False
