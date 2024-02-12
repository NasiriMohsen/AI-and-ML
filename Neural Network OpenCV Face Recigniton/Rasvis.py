from re import X
from stat import FILE_ATTRIBUTE_ENCRYPTED
import cv2 as cv 
from RASFace import Face




FaceRecogniction = Face()
webcam = cv.VideoCapture(0)

def avg(x):
    list1 = []
    for x in range(1,x+1):
        y = 1/x
        list1.append(y)
    avgsum = sum(list1)
    return avgsum


while True:
    MainFrame = webcam.read()[1]
    Faces = FaceRecogniction.FaceDetector(MainFrame)
    average = (99.9 - avg(FaceRecogniction.Datasetlength()))
    #print(average)
    Frame,Facelist = FaceRecogniction.Recogniser(MainFrame,Faces,AverageMatchScore=average)

    print(Facelist)
    cv.imshow("Frame",Frame)
    if ord("q") == cv.waitKey(1):
        cv.destroyAllWindows()
        break
    
