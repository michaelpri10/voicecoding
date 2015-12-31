convert_commands = {"a sine": "assign",
                    "a sign": "assign",
                    "acai": "assign",
                    "assigned": "assign",
                    "Prince": "print",
                    "pretty": "print",
                    "else": "if else command",
                    "elf": "if else command",
                    "Elsa": "if else command",
                    "Ellis": "if elif",
                    "LS": "if elif"}

convert_func_methods = {"perimeters": "parameters",
                        "prams": "parameters",
                        "params": "parameters",
                        "Aaron's": "parameters",
                        "torrents": "parameters",
                        "message": "method"}


# changes words in the voice command to better match what the user is saying
def voice_conversion(speech, time):
    if time == "command":
        for i in convert_commands:
            if speech.startswith(i):
                speech = speech.replace(i, convert_commands[i])
    if time == "function" or time == "method":
        for i in convert_func_methods:
            speech = speech.replace(i, convert_func_methods[i])

    return speech
