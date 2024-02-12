# Chatbot R|A|S Version = 3.0
# Updates: Will Learn if it doesnt understand
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

model = MLPClassifier()
EX = Extractor()


data = EX.Getdata(path)
words = EX.Extract()

3
try :
    model = joblib.load('RAS.pkl')
    print("Loaded model")
except:
    Labels,Features = EX.Encode()
    Features = np.array(Features)
    Labels = np.array(Labels)
    model.fit(Features,Labels)
    joblib.dump(model,'RAS.pkl')
    print("Created model")


print()
print("Hello")
print("My name is: 'R|A|S' ")
print()
while True:
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
        print('I will respond next time! ')

    else:
        print(EX.Response(result))