import cv2 as cv
import numpy as np
from skimage import feature
from sklearn.neural_network import MLPClassifier
import joblib
import datetime as dt
import os

def percent(X):
    percent = int(X*1000)/10
    return percent 

def clearer(path,folder):
    label = path.replace('.jpg','')
    label = label.replace(folder,'')
    label = ''.join([i for i in label if not i.isdigit()])
    label = label.lower()
    return label

class Face():

    def __init__(self):
        #File Directories
        self.FaceDir = "SavedFaces"
        self.CascadeDir = "Face.xml"
        self.SX = 45
        self.SY = 45

        self.FacePaths = []
        self.counter = 0
        self.previ = False
        self.result = ['']
        self.Present = {''}
        self.Features = []
        self.Labels = []
        self.Names = {''}
        
        if self.CascadeDir not in os.listdir():
            print("The Cascade '"+self.CascadeDir+"' was not found")
        else:
            self.TargetCas = cv.CascadeClassifier(self.CascadeDir)
            self.model = MLPClassifier()
            #self.model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

        if self.FaceDir not in os.listdir():
            print("Creating '"+self.FaceDir+"' directory")
            os.mkdir(self.FaceDir)

        if os.listdir(self.FaceDir) != []:
            self.ModelMade = True
            for Facefiles in os.listdir(self.FaceDir):
                self.FacePaths.append(Facefiles)

            #try :
            #    model = joblib.load('saved_model.pkl') 
            #except:
            print(self.FacePaths)
            for Path in self.FacePaths:
                Face = cv.imread("./"+self.FaceDir+"/"+Path)
                Face = cv.resize(Face,(self.SX,self.SY))
                Fvec = feature.hog(Face,channel_axis=-1) 
                self.Features.append(Fvec)
                Label = clearer(Path,self.FaceDir)
                if Label not in self.Names:
                    self.Names.add(Label)
                self.Labels.append(Label)

                self.model.fit(np.array(self.Features),self.Labels)
                joblib.dump(self.model,'saved_model.pkl') 
        else:
            self.ModelMade = False


    def FaceDetector(self,Frame):
        FrameGray = cv.cvtColor(Frame,cv.COLOR_BGR2GRAY)
        
        Faces = self.TargetCas.detectMultiScale(FrameGray,1.1,8)    
        #Faces = self.TargetCas.detectMultiScale(FrameGray)    
        return Faces

    def Datasetlength(self):
        return len(os.listdir(self.FaceDir))    

    def Recogniser(self,Frame,Faces,AverageMatchScore=75,Alpha=0.05,Visual=True,FaceLearner=True):
        FrameCopy = Frame.copy()
        Facelist = []
        if len(Faces) > 0:
            Scorelist = []
            for (x,y,w,h) in Faces:
                RoI = Frame[y:y+h,x:x+w]
                RoI2 = cv.resize(RoI,(self.SX,self.SY))
                Fvec = feature.hog(RoI2,channel_axis=-1)
                if Visual == True:
                    cv.rectangle(FrameCopy,(x,y),(x+w,y+h),(255,0,0),2)
                
                if self.ModelMade == True:
                    Score = self.model.predict_proba(np.array(Fvec.reshape(1, -1)))
                    for smt in Score[0]:
                        Scorelist.append(percent(smt))

                    if Visual == True:
                        cv.putText(FrameCopy, 'Score: '+str(max(Scorelist)), (x,y+h+40), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255), 1)

                    if max(Scorelist) < AverageMatchScore:
                        if self.previ == False:
                            self.counter = self.counter + 1
                            self.previ = True

                        Facelist.append(("Unknown Face",max(Scorelist)))

                        if Visual == True:
                            cv.putText(FrameCopy, 'Unknown'+str(self.counter), (x,y+h+25), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 255), 1)

                        if FaceLearner == True:
                            Label = input("Unknown Face! Who is this? ")
                            AverageMatchScore = AverageMatchScore - Alpha
                            Label = clearer(Label,self.FaceDir)
                            self.Labels.append(Label)
                            self.Features.append(Fvec)
                            self.model.fit(np.array(self.Features),self.Labels)
                            date = ((dt.datetime.now().strftime("%X")).replace(':','')) + ((dt.datetime.now().strftime("%x")).replace('/',''))
                            Filename = Label + date +'.jpg'
                            cv.imwrite("./"+self.FaceDir+"/"+Filename,RoI2)        
                                            

                    else:    
                        Result = self.model.predict(np.array(Fvec).reshape(1, -1))
                        if Result[0] not in self.Present:
                            self.Present.add(Result[0])
                        Result = Result[0][0].upper()+Result[0][1:]
                        Facelist.append((Result,max(Scorelist)))
                        if Visual == True:
                            cv.putText(FrameCopy,Result, (x,y+h+25), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 255), 1)
                else:
                    Face = Frame[y:y+h,x:x+w]
                    Face = cv.resize(Face,(self.SX,self.SY))
                    Fvec = feature.hog(Face,channel_axis=-1)
                    Label = input("Unknown Face! Who is this? ")
                    Label = clearer(Label,self.FaceDir)
                    self.Labels.append(Label)
                    self.Features.append(Fvec)
                    self.model.fit(np.array(self.Features),self.Labels)
                    date = ((dt.datetime.now().strftime("%X")).replace(':','')) + ((dt.datetime.now().strftime("%x")).replace('/',''))
                    Filename = Label + date +'.jpg'
                    cv.imwrite("./"+self.FaceDir+"/"+Filename,Face)   
                    self.ModelMade = True   
        else:
            self.pervi = False
        
        return FrameCopy,Facelist