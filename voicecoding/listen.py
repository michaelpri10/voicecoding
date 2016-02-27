import sys
import speech_recognition as sr
from .eval_command import eval_command
from .code_class import Code
from .exec_output import exec_output
from .helpers.get_terminal_size import get_terminal_size

# initialize the mic and the speech recognizer
r = sr.Recognizer()
m = sr.Microphone()


def main():
    try:
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            while True:
                # clears screen
                print("\n" * (get_terminal_size()[1]+10))
                # prints out previous code and errors
                for i in Code.output:
                    if i != '':
                        print(i)
                print("-" * get_terminal_size()[0])
                for i in Code.errors:
                    print(i)
                Code.errors = []
                # listens for voice
                print("\nCommand: ")
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
                    Code.errors.append("You said: {0}".format(command))
                    # updates code if Code.multine is True
                    # saves it for assigning to code otherwise
                    temp_code = eval_command(command)
                    if Code.multiline is False:
                        Code.if_else_loop = False
                        Code.code = temp_code
                    if Code.code:
                        # checks if code is multiline
                        if Code.multiline is True:
                            current_line = Code.code[len(Code.code)-1]
                            if (current_line.strip() != "end" and
                                    current_line != Code.last_line):
                                if len(Code.code) == 1:
                                    Code.output.append(">>> {0}".format(
                                        current_line
                                    ))
                                    Code.last_line = current_line
                                else:
                                    Code.output.append("... {0}".format(
                                        current_line
                                    ))
                                    Code.last_line = current_line
                            # if the last line is 'end', run the code
                            if Code.code[len(Code.code)-1] == "end":
                                to_exec = "{0}\n".format(Code.code[0])
                                for i in range(1, len(Code.code)-1):
                                    # skip the code if it is an 'end' statement
                                    if Code.code[i].strip() == ("end"):
                                        pass
                                    else:
                                        to_exec += "{0}\n".format(Code.code[i])
                                # resets Code
                                Code.multiline = False
                                Code.code = ""
                                Code.if_else_loop = False
                                Code.def_func = False
                                for i in Code.loop_func_vars:
                                    Code.defined_vars.remove(i)
                                Code.loop_func_vars = []

                                # executes the code
                                Code.output.append(exec_output(to_exec))
                                sys.stdout = sys.__stdout__
                        else:
                            # executes the code
                            Code.output.append(">>> {0}".format(Code.code))
                            Code.output.append(exec_output(Code.code))
                            sys.stdout = sys.__stdout__
                    else:
                        if Code.code is None:
                            pass
                        else:
                            Code.errors.append("Invalid command")

                except sr.UnknownValueError:
                    Code.errors.append("Oops! Didn't catch that")
                except sr.RequestError as e:
                    Code.errors.append("""Uh oh! Couldn't request
                                          results from Google
                                          Speech Recognition service;
                                          {0}""".format(e))
    except KeyboardInterrupt:
        pass
