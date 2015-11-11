from commands import commands

def eval_command(command):
    instruction = command.split()[0]
    print(instruction)
    to_parse = " ".join(command.split()[1:])
    print(to_parse)
    if instruction in commands:
        return commands[instruction](to_parse)
    else:
        return False
