convert_at_beginning = {"a sine": "assign",
                        "assigned": "assign" 
                       }

def voice_conversion(speech, time):
    if time == "beginning":
        for i in convert_at_beginning:
            speech = speech.replace(i, convert_at_beginning[i])

    return speech
