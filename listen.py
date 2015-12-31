import speech_recognition as sr
from eval_command import eval_command
from code_class import Code

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
                temp_code = eval_command(command)
                if not Code.multiline:
                    Code.code = temp_code
                    Code.if_else = False
                print(Code.code)
                if Code.code:
                    if Code.multiline is True:
                        if Code.code[len(Code.code)-1] == "end":
                            print(">>> {0}".format(Code.code[0]))
                            to_exec = "{0}\n".format(Code.code[0])
                            for i in range(1, len(Code.code)-1):
                                print("... {0}".format(Code.code[i]))
                                to_exec += "{0}\n".format(Code.code[i])
                            Code.multiline = False
                            Code.code = ""
                            Code.if_else = False
                            try:
                                exec(to_exec)
                            except Exception as e:
                                print(e.__doc__)
                                print(e)

                    else:
                        print(">>> {0}".format(Code.code))
                        try:
                            exec(Code.code)
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
