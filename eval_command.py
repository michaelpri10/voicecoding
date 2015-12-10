from commands import commands

def eval_command(command):
    instruction = command.split()[0]
    if instruction.lower() == "exit":
        print("Exiting...")
        quit()
    if len(command.split()) == 1:
        return False
    to_parse = " ".join(command.split()[1:])
    if instruction in commands:
        return commands[instruction](to_parse)
    else:
        return False
