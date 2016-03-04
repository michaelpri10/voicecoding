convert_commands = {"a sine": "assign",
                    "a sign": "assign",
                    "acai": "assign",
                    "assigned": "assign",
                    "Prince": "print",
                    "pretty": "print",
                    "Sprint": "print",
                    "printex": "print x",
                    "printer": "print i",
                    "else": "if else command",
                    "elf": "if else command",
                    "Elsa": "if else command",
                    "elif": "if elif",
                    "Ellis": "if elif",
                    "LS ": "if elif",
                    "LF": "if elif",
                    "4": "for ",
                    "phone": "for",
                    "wild": "while",
                    "Define": "define",
                    "returnx": "return x"}

convert_func_methods = {"perimeters": "parameters",
                        "prams": "parameters",
                        "params": "parameters",
                        "Aaron's": "parameters",
                        "torrents": "parameters",
                        "Graham's": "parameters",
                        "program": "parameters",
                        "programs": "parameters",
                        "message": "method"}

convert_data_types = {"equations": "equation"}

convert_if_else_loops = {}


# changes words in the voice command to better match what the user is saying
def voice_conversion(speech, time):
    if time == "command":
        # hardcoded for `if` statements
        if speech.startswith("is"):
            speech = "if" + speech[2:]
        for i in convert_commands:
            if speech.startswith(i):
                speech = speech.replace(i, convert_commands[i])
    if time == "function" or time == "method":
        for i in convert_func_methods:
            speech = speech.replace(i, convert_func_methods[i])
    if time == "data_type":
        for i in convert_data_types:
            speech = speech.replace(i, convert_data_types[i])
    if time == "if-else/loop":
        for i in convert_if_else_loops:
            speech = speech.replace(i, convert_if_else_loops[i])

    return speech
