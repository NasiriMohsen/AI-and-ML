# Chatbot R|A|S Version = 3.2
# Updates: It Learns from start
#############################################################
import numpy as np 
from Extractor import Extractor
from sklearn.neural_network import MLPClassifier


def percent(X):
    percent = int(X*1000)/10
    return percent 


avgscore = 92
path = "dataset.json"
learn = True

model = MLPClassifier()
EX = Extractor()
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
        print(EX.Response(result),score)