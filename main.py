import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Please Speak")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
            if 'siri' in command:
                print('I am Better than SIRI')
    except:
        pass
    return command


def run_alexa():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p ')
        talk("Current time is " + time)
    elif 'wikipedia' or 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' or 'Stop' in command:
        print(command)
        exit()
    else:
        talk("Please repeat the command")


while True:
    run_alexa()


# Install Following packages ( Commands are given below ) Project required python 3.6 or lower 
# 1. Python Pyaudio - pip install PyAudio
# 2. Python text-to-speech - pip install pyttsx3
# 3. Python speech recognition - pip install SpeechRecognition
# 4.Python PyWhatKit - pip install pywhatkit
# 5. Python Wikipedia - pip install wikipedia
# 6. Python Jokes - pip install pyjokes
