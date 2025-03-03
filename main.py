import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "search" in command:
        speak("What do you want to search for?")
        with sr.Microphone() as source:
            print("Listening for search query...")
            try:
                audio = recognizer.listen(source, timeout=5)
                search_query = recognizer.recognize_google(audio)
                speak(f"Searching for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand that. Please try again.")
            except sr.RequestError:
                speak("There was an error with the speech recognition service.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

if __name__ == "__main__":
    speak("Hello, I am Jarvis, your personal assistant!")

    while True:
        try:
            with sr.Microphone() as source:
                print("Say 'Jarvis' to activate...")
                audio = recognizer.listen(source, timeout=5)
                wake_word = recognizer.recognize_google(audio).lower()

                if "jarvis" in wake_word:
                    speak("Yes, how can I assist?")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)

        except sr.UnknownValueError:
            print("Didn't catch that. Please try again.")
        except sr.RequestError:
            print("Speech recognition service error.")
        except KeyboardInterrupt:
            speak("Goodbye!")
            break
