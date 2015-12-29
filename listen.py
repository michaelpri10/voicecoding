import speech_recognition as sr
from eval_command import eval_command

# initialize the mic and the speech recognizer
r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
        while True:
            # listens for voice
            print("Command: ")
            audio = r.listen(source)
            print("Recognizing...")
            try:
                # recognizes speech using Google Speech Recognition
                value = r.recognize_google(audio)

                # adds str compatibilty for Python 2
                if str is bytes:
                    command = value.encode("utf-8")
                else:
                    command = value
                # prints command for debugging
                print(command)
                # converts the voice command to Python code and runs it
                code = eval_command(command)
                if code:
                    print(">>> {0}".format(code))
                    try:
                        exec(code)
                    # prevents crashing on code error
                    except Exception as e:
                        print(e.__doc__)
                        print(e)

                else:
                    print("Invalid command")

            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("""Uh oh! Couldn't request results from
                         Google Speech Recognition service; {0}""".format(e))
except KeyboardInterrupt:
    pass
