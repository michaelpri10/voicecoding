import speech_recognition as sr
from eval_command import eval_command

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
        while True:
            print("Command: ")
            audio = r.listen(source)
            print("Recognizing...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)

                if str is bytes:
                    command = value.encode("utf-8")
                else:
                    command = value
                
                print(command)
                code = eval_command(command)
                print(code)
                if code:
                    pass
                else:
                    print("Invalid command")

            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
