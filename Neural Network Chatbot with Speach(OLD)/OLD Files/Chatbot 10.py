# Chatbot R|A|S Version = 1.0
# First attempt
#############################################################
import numpy as np 
import random
from Extractor import Extractor
from sklearn.neural_network import MLPClassifier


def percent(X):
    percent = int(X*1000)/10
    return percent 


avgscore = 60


model = MLPClassifier()
EX = Extractor()


data = EX.Getdata("intents.json")
words = EX.Extract()
Labels,Features = EX.Encode()
Features = np.array(Features)
Labels = np.array(Labels)


model.fit(Features,Labels)


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
        response = 'I dont know what that means!'
    else:
        for smt in data["intents"]:
            if smt['tag'] == result:
                responses = smt['responses']
                response = random.choice(responses)
    print(response,score)