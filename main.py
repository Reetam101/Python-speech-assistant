import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound, os, random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            brain_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:   
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            brain_speak('Sorry, I did not get that') 
        except sr.RequestError:
            brain_speak('Sorry, the service is down')       
        return voice_data   

def brain_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        brain_speak('My name is Dash')
    if 'what time is it' in voice_data:
        t = list(ctime().split())
        brain_speak(t[3])    
    if 'what day is it' in voice_data:
        t = list(ctime().split())
        if t[0] == 'Mon':
            brain_speak('Monday')
        elif t[0] == 'Tue':
            brain_speak('Tuesday')
        elif t[0] == 'Wed':
            brain_speak('Wednesday') 
        elif t[0] == 'Thu':
            brain_speak('Thursday')
        elif t[0] == 'Fri':
            brain_speak('Friday')
        elif t[0] == 'Sat':
            brain_speak('Saturday')
        else:
            brain_speak('Sunday')                            
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = f'https://google.com/search?q={search}'  
        webbrowser.get().open(url)
        brain_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        search = record_audio('What is the location?')
        url = f'https://google.nl/maps/place/{search}/&amp'  
        webbrowser.get().open(url)
        brain_speak('Here is the location of ' + search) 
    if 'exit' in voice_data:
        exit()       
            
time.sleep(1)
brain_speak('How can I help you?')
while 1:
    voice_data = record_audio()    
    respond(voice_data)