# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3 
r = sr.Recognizer() 
def SpeakText(command):
    
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    

while(1):    
    try:

        with sr.Microphone() as source2:
            
            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print(&quot;Did you say &quot;,MyText)
            SpeakText(MyText)
            
    except sr.RequestError as e:
        print(&quot;Could not request results; {0}&quot;.format(e))
        
    except sr.UnknownValueError:
        print(&quot;unknown error occurred&quot;)
