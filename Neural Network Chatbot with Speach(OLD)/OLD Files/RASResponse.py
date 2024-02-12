import os
import time
import pyttsx3

class Response:
    def __init__(self):
        #self.directory = os.system('cd')
        self.engine = pyttsx3.init()

    def speak(self,msg,Input=False):
        if Input == False:
            print(msg)
            self.engine.say(msg)
            self.engine.runAndWait()
        else:
            self.engine.say(msg)
            self.engine.runAndWait()
            return input(msg)

    def Respond(self,msg):
        msg = msg.lower()
        if msg == 'hello':
            self.speak("Hi Sir! What can I do for you?")
        
        elif msg == 'time':
            self.speak(str(time.asctime( time.localtime(time.time()) )))

        elif msg == 'open':
            name = self.speak("whats the name? ",Input=True)
            os.system('start '+ name)

        elif msg == 'directory':
            dire = self.speak("whats the directory? ",Input=True)
            os.system('cd '+ dire)
            self.speak("done")

        elif msg == 'desktop':
            os.system('cd C:/Users/Asus/Desktop')
            self.speak("done")
        
        elif msg == 'speak':
            text = self.speak("whats should I say? ",Input=True)
            self.speak(text)

        elif msg == 'popup':
            text = self.speak("whats should it say? ",Input=True)
            os.system("msg * " + text)