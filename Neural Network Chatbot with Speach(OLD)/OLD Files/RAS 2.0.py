# Chatbot R|A|S Version = 2.0
# Updates: He can speak any thing
#############################################################
import numpy as np 
from Extractor import Extractor
from sklearn.neural_network import MLPClassifier
from RASResponse import Response

def percent(X):
    percent = int(X*1000)/10
    return percent 

Name = "Ras"
RASavgscore = 92
avgscore = 70
RASpath = "Rasdataset.json"
path = "Dialogue.json"
learn = True
RASlearn = True
RASmodel = MLPClassifier()
model = MLPClassifier()
RAS = Extractor()
EX = Extractor()
RASdata = RAS.Getdata(RASpath)
data = EX.Getdata(path)
responder = Response()

print()
responder.speak("Hello")
responder.speak("I am Raas. What can I do for you sir?")
print()
while True:
    if learn == True:
        EX.Upgradedata(path)
        words = EX.Extract()
        Labels,Features = EX.Encode()
        model.fit(np.array(Features),np.array(Labels))
        learn = False
    if RASlearn == True:
        RAS.Upgradedata(RASpath)
        RASwords = RAS.Extract()
        RASLabels,RASFeatures = RAS.Encode()
        RASmodel.fit(np.array(RASFeatures),np.array(RASLabels))
        RASlearn = False
    
    msg = input(" You: ")
    print()
    firstword = msg.split(' ')[0].lower()
    
    
    if firstword != Name.lower(): 
        feature = EX.SentenceEncoder(msg,words)
        feature = [np.array(feature)]
        result = model.predict(feature)[0]
        score = percent(max(model.predict_proba(feature)[0]))
        if score < avgscore:
            responder.speak('Sir, what does that mean? ')
            print(score)
            learn = EX.Learn(msg)
            
        else:
            responder.speak(EX.Response(result))
            print(score)

    else:
        feature = RAS.SentenceEncoder(msg,RASwords)
        feature = [np.array(feature)]
        result = RASmodel.predict(feature)[0]
        score = percent(max(RASmodel.predict_proba(feature)[0]))
        if score < RASavgscore:
            responder.speak('Sir, what does that mean? ')
            print(score)
            RASlearn = RAS.Learn(msg)
            
            
        else:
            responder.speak(RAS.Response(result))
            print(score)
            responder.Respond(result)
