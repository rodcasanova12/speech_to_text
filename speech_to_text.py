import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()


def record_text():
    # Loop in case of errors
    while (1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("Please say something")

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")
    return


def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()

    return


while (1):
    text = record_text()
    output_text(text)

    print("You said: {}".format(text))
