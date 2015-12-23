convert_commands = {"a sine": "assign",
                    "assigned": "assign" 
                   }

def voice_conversion(speech, time):
    if time == "command":
        for i in convert_commands:
            if speech.startswith(i):
                speech = speech.replace(i, convert_commands[i])

    return speech
