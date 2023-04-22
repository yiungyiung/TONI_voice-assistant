import speech_recognition as speech
from gtts import gTTS
from io import BytesIO
from playsound import playsound
import os
import wolframalpha
import wikipedia
import webbrowser
from datetime import datetime
import pyjokes
import win32api 
import time

#converting speech to text
appid='3GX548-6H6Q382UYW'
client = wolframalpha.Client(appid)
def audio():
    print('Listening')
    #response('listening')
    a=speech.Recognizer()
    voice=speech.Microphone()
    with voice:
        try:
            record=a.listen(voice)
            data=''
            data=a.recognize_google(record)
            if 'tony' in data.lower() or 'dhoni' in data.lower():
                data=data.lower()
                data=data.replace("dhoni","")
                l=data.split("tony")
                m=l[0]
                for i in l:
                    if len(i)>len(m):
                        m=i
                #print(m)###data res()
                dataresponse(m)
                ##response(m)
            else:
                print(data)
                response("use tony before your query")
        except speech.UnknownValueError:
            print("Sorry tony is dumb")
            response('try again')
        return data          
def response(aud):
    try:
        #print(aud)
        ans=gTTS(text=aud, lang='en',tld="com.au")
        file="1"+".mp3"
        ans.save(file)
        playsound(file)
        os.remove(file)
    except:
        ans=gTTS(text='sorry i dont know about this', lang='en',tld="com.au")
        file="1"+".mp3"
        ans.save(file)
        playsound(file)
        os.remove(file)
        
def dataresponse(data): 
    if "wikipedia" in data and "search" in data :
        l=data.split()
        if "search" in l:
            if 'search for' in data:
                l.remove('search')
                l.remove('for')
            else:
                l.remove('search')
        data=' '.join(l)
        if "wikipedia for" in data:
            l=data.split("wikipedia for")
        else:
            l=data.split("on wikipedia")
        print(l)
        m=l[0]
        for i in l:
            if len(i)>len(m):
                m=i
        result = wikipedia.summary(m, sentences = 2)
        print(result)
        response(result)
    elif "youtube" in data and ('open' in data or "search" in data or'play' in data):
        if "open" in data:
             webbrowser.open_new("https://www.youtube.com")
        else:
            l=data.split()
            if "search" in l:
                if 'search for' in data:
                    l.remove('search')
                    l.remove('for')
                else:
                    l.remove('search')
            elif 'play' in l:
                l.remove('play')
            data=' '.join(l)
            if "youtube for" in data:
                l=data.split("youtube for")
            else:
                l=data.split("on youtube")
            print(l)
            m=l[0]
            for i in l:
                if len(i)>len(m):
                    m=i
            response("searching "+m+" on YouTube")
            webbrowser.open_new("https://www.youtube.com/results?search_query="+"+".join(m.split()))
    elif "google" in data and ("open" in data or "search" in data):
        if "open" in data:
             webbrowser.open_new("https://www.google.com")
        else:
            data=data.replace("search",'')
            if "google for" in data:
                l=data.split("google for")
            else:
                l=data.split("on google")
                print(l)
                m=l[0]
            for i in l:
                if len(i)>len(m):
                    m=i
            response("searching "+m+" on Google")
            webbrowser.open_new("https://www.google.com/search?q="+"+".join(m.split()))
    elif "gmail" in data and ("open" in data or "search" in data):
        if "open" in data:
             webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")
    elif "prime video" in data and ("open" in data or "search" in data or 'play' in data):
        if "open" in data:
             webbrowser.open_new("https://www.primevideo.com")
        else:
            l=data.split()
            if "search" in l:
                if 'search for' in data:
                    l.remove('search')
                    l.remove('for')
                else:
                    l.remove('search')
            elif 'play' in l:
                l.remove('play')
            data=' '.join(l)
            if "prime video for" in data:
                l=data.split("prime video for")
            else:
                l=data.split("on prime video")
            print(l)
            m=l[0]
            for i in l:
                if len(i)>len(m):
                    m=i
            response("searching "+m+" on Prime Video")
            webbrowser.open_new("https://www.primevideo.com/search/ref=atv_nb_sr?phrase="+"+".join(m.split())+"&ie=UTF8")
    elif "hotstar" in data and ("open" in data or "search" in data or 'play' in data):
        if "open" in data:
             webbrowser.open_new("https://www.hotstar.com")
        else:
            l=data.split()
            if "search" in l:
                if 'search for' in data:
                    l.remove('search')
                    l.remove('for')
                else:
                    l.remove('search')
            elif 'play' in l:
                l.remove('play')
            data=' '.join(l)
            if "hotstar for" in data:
                l=data.split("hotstar for")
            else:
                l=data.split("on hotstar")
            print(l)
            m=l[0]
            for i in l:
                if len(i)>len(m):
                    m=i
            response("searching "+m+" on Hotstar")
            webbrowser.open_new("https://www.hotstar.com/in/search?q="+"%20".join(m.split()))
    elif 'joke' in data and ("tell" in data or "crack" in data):
        s=pyjokes.get_joke()
        print(s)
        response(s)
    elif "spotify" in data and ('open'in data or "search" in data or 'play' in data):
        if "open" in data:
             webbrowser.open_new("https://open.spotify.com/")
        else:
            l=data.split()
            if "search" in l:
                if 'search for' in data:
                    l.remove('search')
                    l.remove('for')
                else:
                    l.remove('search')
            elif 'play' in l:
                l.remove('play')
            data=' '.join(l)
            if "spotify for" in data:
                l=data.split("spotify for")
            else:
                l=data.split("on spotify")  
            print(l)
            m=l[0]
            for i in l:
                if len(i)>len(m):
                    m=i
            response("searching "+m+" on spotify")
            webbrowser.open_new("https://open.spotify.com/search/"+"%20".join(m.split()))      
    elif 'how are you' in data:
        print('I am feeling great how about you')
        response('I am feeling great how about you')
    elif "who are you" in data or "tell me about you" in data or "tell me something about you" in data:
        print("Hi!, I am Toni, short for 'Totally Overrated Noise initiator', I can perform simple tasks such as calculations, search on different platforms, I can rick roll you on youtube as well as play sad songs when you found out you are getting a CNG in semester one")
        response("Hi!, I am Toni, short for 'Totally Overrated Noise initiator', I can perform simple tasks such as calculations, search on different platforms, I can rick roll you on youtube as well as play sad songs when you found out you are getting a CNG in semester one")
        
        
    elif 'exit' in data or 'shut up' in data:
        response("awwwwww sucks  bye bye")
        print('bye bye')
        global exitu
        exitu=False
    else:
        print(data)
        res = client.query(data)
        print(next(res.results).text)
        response(str(next(res.results).text))
    print("done command")
#audio()
state_left = win32api.GetKeyState(0x02)
print('Toni is now functioning')
exitu=True
while (exitu): 
    a = win32api.GetKeyState(0x02)
    if a != state_left:  # Button state changed 
        state_left = a 
        #print(a) 
        if a < 0: 
            #print('Tony has been started')
            audio()
