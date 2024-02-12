#EX = extractor()
#data = EX.Getdata("intents.json")
#words = EX.Extract(data)
#Labels,Features = EX.Encode()
#model.fit(np.array(Features),Labels)
#feature = EX.SentenceEncoder(input,words)
#result = model.perdict(feature)
###########################################################
import json
import random
import pyttsx3

class Extractor:
    def __init__(self):
        self.data = {}
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

    def Getdata(self,Path):
        try:
            with open(Path) as file:
                self.data = json.load(file)
        except:
            with open(Path,'w') as file:
                self.data = {}
                self.data['intents'] = []
                self.data['intents'].append({"tag":"hello","patterns":["hello","hi","hey"],"responses":["hello sir","hi sir"]})
                json.dump(self.data,file,indent=4)
        return self.data

    def Givedata(self,Data):
        self.data = Data
    
    def Extract(self):
        self.words = []
        self.xfeature = []
        self.ylabel = []
        for intent in self.data["intents"]:
            for pattern in intent["patterns"]:
                wrds = pattern.split(' ')
                self.words.extend(wrds)
                self.xfeature.append(wrds)
                self.ylabel.append(intent["tag"])
        self.words = [w.lower() for w in self.words]
        self.words = sorted(list(set(self.words)))
        return self.words
    
    def Encode(self):
        self.Features = []
        self.Labels = []
        for x,words in enumerate(self.xfeature):
            wrds = [w.lower() for w in words]
            kwords = []
            for w in self.words:
                if w in wrds:
                    kwords.append(1)
                else:
                    kwords.append(0)
            self.Features.append(kwords)
            self.Labels.append(self.ylabel[x]) 
        return self.Labels,self.Features

    def SentenceEncoder(self,Sentence,Words):
        feature = [0 for _ in range(len(Words))]
        words = Sentence.split(' ')
        wrds = [w.lower() for w in words]
        for w in wrds:
            for i,x in enumerate(Words):
                if x == w:
                    feature[i] = 1
        return feature
    
    def Response(self,Tag):
        for smt in self.data["intents"]:
            if smt['tag'] == Tag.lower():
                responses = smt['responses']
                response = random.choice(responses)
                return response
    
    def Learn(self,Sentence):
        flag = False
        tag = self.speak("What is the intention of this Sentence? ",Input=True)
        tag = tag.lower()
        if tag == "cancel":
            self.speak("Canceled")
            return False
        response = self.speak("What should I respond with? ",Input=True)
        response = response.lower()
        if response == "cancel":
            self.speak("Canceled")
            return False
        for smt in self.data["intents"]:
            if smt['tag'] == tag:
                if response not in smt['responses']:
                    smt['responses'].append(response)
                if Sentence not in smt['patterns']:
                    smt['patterns'].append(Sentence.lower())
                flag = True
                break
        if flag == False:
            self.data['intents'].append({"tag":tag,"patterns":[Sentence],"responses":[response]})
        self.speak("I have Learned that")
        return True

    def Upgradedata(self,Path):
        with open(Path,'w') as file:
            json.dump(self.data,file,indent=4)






