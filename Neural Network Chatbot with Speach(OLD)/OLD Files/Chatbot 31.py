# Chatbot R|A|S Version = 3.1
# Updates: It Learns atm
#############################################################
import numpy as np 
from Extractor import Extractor
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib


def percent(X):
    percent = int(X*1000)/10
    return percent 


avgscore = 60
path = "intents.json"
learn = True

model = MLPClassifier()
EX = Extractor()

print()
print("Hello")
print("My name is: 'R|A|S' ")
print()
while True:
    if learn == True:
        data = EX.Getdata(path)
        words = EX.Extract()
        Labels,Features = EX.Encode()
        model.fit(np.array(Features),np.array(Labels))
        learn = False


    msg = input("Your message: ")
    print()


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
        print(EX.Response(result))