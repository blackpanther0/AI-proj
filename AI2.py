 
import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0])

def speak(audio):
    print('bot :',audio)
    engine.say(audio)
    engine.runAndWait()

speak("hello welcome to doctor's advicor")

speak("Please enter your name ->")
name=input()

speak(f'hello {name} nice to meet you')
speak("which mode you want to chat by text or by voice")
speak('press 1 for chat or press 2 for voice ->')
x=int(input())

def docomm():
    
    if x==2:
        speak("please on your internet")
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                print("say HEY GHOST to activate")
                ret=r.recognize_google(audio,language='eng-us')
                print(ret)
            except:
                ret=None
                docomm()
            return ret.lower()
    elif x==1:
        txt=input(f'{name} :')
        return txt.lower()

speak("what made you to come hear")

symptoms=[]
def disease():
    print("you symptoms are")
    print(symptoms)
    if 'fever' in symptoms:
        if 'cold' in symptoms:
            speak("you may have corona virus")
            speak("your self isolated and call nearby hospial")
    elif 'cold' in symptoms:
        if 'headache' in symptoms:
            if 'temprature' in symptoms:
                speak("you may have fever")
                speak("you have to take PARACETMOL")
            else:
                speak("you may have headache")
                speak("you have to take zero DAL P")
        else:
            speak("you may have common  cold")
            speak("you can take PARACETMOL")
    elif 'stomachache' in symptoms:
         if 'gas' in symptoms:
             speak("It might be gas problem cause you have skipped your meal right?")
             speak("you have to drink ENO with glass of water")
         else:
             speak("you ate junk food right? i think you got motions ")
             speak("you have to take METROGEL")


while(True):
    ret=docomm()
    if 'fever' in ret:
        symptoms.append('fever')
    elif 'stomachache' in ret:
        symptoms.append('stomachache')
    elif 'gas' in ret:
        symptoms.append('gas')
    elif 'headache' in ret:
        symptoms.append('headache')
    elif 'temprature' in ret:
        symptoms.append('temprature')    
    elif 'cold' in ret:
        symptoms.append('cold')
    elif 'nothing' in ret:
        disease()
        speak("take care of yourself")
        input("press enter to exit")
        exit()
    elif 'good' in ret:
        speak("thats really good to hear")
        speak("we are kinda busy we will catch you up thankyou")
        exit()
    speak("what else symptoms do you have")
