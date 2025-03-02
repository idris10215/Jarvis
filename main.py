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
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            command = r.recognize_google(audio)
            print(command)
        except Exception as e:
            print("Error; {0}".format(e))        