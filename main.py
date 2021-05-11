import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('I am your Ruby')
engine.say('What can I do for You')
engine.runAndWait()

def take_command():
    try:
        with sr.Microphone as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Ruby' in command:
                command = command.replace('Ruby','')
                talk(command)

    except:
        pass
    return command
    def run_Ruby():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play','')
            talk('playing '+ song)
            pywhatkit.playonyt('song')
        elif 'time' in command:
            time = datetime.datetime.noe().strftime('%I:%M %p')
            print(time)
            talk('Current time is' + time)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is','')
            info = wikipedia.summary(person,1)
            print(info)
            talk(info)


    run_Ruby()