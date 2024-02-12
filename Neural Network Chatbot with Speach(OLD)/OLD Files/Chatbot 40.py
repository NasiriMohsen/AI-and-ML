# Chatbot R|A|S Version = 40
# Updates: Read from two datasets
#############################################################
import numpy as np 
from Extractor import Extractor
from sklearn.neural_network import MLPClassifier


def percent(X):
    percent = int(X*1000)/10
    return percent 

Name = "Ras"
RASavgscore = 92
avgscore = 92
RASpath = "dataset2.json"
path = "dataset.json"
learn = True
RASlearn = True
RASmodel = MLPClassifier()
model = MLPClassifier()
RAS = Extractor()
EX = Extractor()
RASdata = RAS.Getdata(RASpath)
data = EX.Getdata(path)


print()
print("Hello")
print("My name is: 'R|A|S' ")
print()
while True:
    if learn == True:
        words = EX.Extract()
        Labels,Features = EX.Encode()
        model.fit(np.array(Features),np.array(Labels))
        learn = False
    if RASlearn == True:
        RASwords = RAS.Extract()
        RASLabels,RASFeatures = RAS.Encode()
        RASmodel.fit(np.array(RASFeatures),np.array(RASLabels))
        RASlearn = False

    msg = input("Your message: ")
    print()
    firstword = msg.split(' ')[0].lower()
    
    
    if firstword != Name.lower(): 
        feature = EX.SentenceEncoder(msg,words)
        feature = [np.array(feature)]
        result = model.predict(feature)[0]
        score = percent(max(model.predict_proba(feature)[0]))
        if score < avgscore:
            print('I didnt get that! ',score)
            EX.Learn(msg)
            EX.Upgradedata(path)
            learn = True
        else:
            print(EX.Response(result),score)

    else:
        feature = RAS.SentenceEncoder(msg,RASwords)
        feature = [np.array(feature)]
        result = RASmodel.predict(feature)[0]
        score = percent(max(RASmodel.predict_proba(feature)[0]))
        if score < RASavgscore:
            print('I didnt get that! ',score)
            RAS.Learn(msg)
            RAS.Upgradedata(RASpath)
            RASlearn = True
        else:
            print(RAS.Response(result),score)
    
