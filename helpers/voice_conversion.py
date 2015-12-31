convert_commands = {"a sine": "assign",
                    "acai": "assign",
                    "assigned": "assign",
                    "Prince": "print",
                    "pretty": "print",
                    "is": "if",
                    "else": "if else command",
                    "elf": "if else command",
                    "Elsa": "if else command"}

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
