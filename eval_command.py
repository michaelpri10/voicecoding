from instructions import instructions
from helpers.voice_conversion import voice_conversion
from code_class import Code


# evaluates the voice command
def eval_command(command):
    # checks for the instruction
    command = voice_conversion(command, "command")
    instruction = command.split()[0]
    # exits if instruction is "exit"
    if instruction.lower() == "exit":
        print("Exiting...")
        quit()
    if instruction.lower() == "end":
        if Code.multiline:
            Code.code[len(Code.code)] = "end"
        return

    # if there is nothing after the instruction, invalid command
    if len(command.split()) == 1:
        return False

    # gets and runs voice command that will be used with the instruction
    to_parse = " ".join(command.split()[1:])
    if instruction in instructions:
        if Code.if_else:
            if instructions[instruction](to_parse) is not None:
                Code.code[len(Code.code)] = "    {0}".format(
                    instructions[instruction](to_parse))
            return "Continue if-else"
        else:
            return instructions[instruction](to_parse)
    else:
        return False
