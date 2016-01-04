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
                # updates code if Code.multine is True
                # saves it for assigning to code otherwise
                temp_code = eval_command(command)
                if Code.multiline is False:
                    Code.if_else_loop = False
                    Code.code = temp_code
                # prints code for debugging
                print(Code.code)
                if Code.code:
                    # checks if code is multiline
                    if Code.multiline is True:
                        # if the last line is 'end', run the code
                        if Code.code[len(Code.code)-1] == "end":
                            print(">>> {0}".format(Code.code[0]))
                            to_exec = "{0}\n".format(Code.code[0])
                            for i in range(1, len(Code.code)-1):
                                # skip the code if it is an 'end' statement
                                if Code.code[i].strip() == ("end"):
                                    pass
                                else:
                                    print("... {0}".format(Code.code[i]))
                                    to_exec += "{0}\n".format(Code.code[i])
                            # resets Code
                            Code.multiline = False
                            Code.code = ""
                            Code.if_else_loop = False
                            Code.def_func = False
                            for i in Code.loop_func_vars:
                                Code.defined_vars.remove(i)
                            Code.loop_func_vars = []
                            try:
                                exec(to_exec)
                            # prevent code from crashing on an error
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
                    if Code.code is None:
                        pass
                    else:
                        print("Invalid command")

            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("""Uh oh! Couldn't request results from
                         Google Speech Recognition service; {0}""".format(e))
except KeyboardInterrupt:
    pass
