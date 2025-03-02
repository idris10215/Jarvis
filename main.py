import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Hello, I am Jarvis your personal assistant")

    while True:

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...s")
            audio = r.listen(source)

        # recognize speech using Sphinx
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))        