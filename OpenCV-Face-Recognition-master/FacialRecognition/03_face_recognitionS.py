
import cv2
import numpy as np
import os 
from google_speech import Speech
import time
import tkinter.messagebox


NonSpeech=""
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml")
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

lang = "en"

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

names= ['NULL','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE']

temp=''
for root,dirs,files in os.walk("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"):
	for filename in files:
		temp=filename.split('.')[0]
		temp1=int(filename.split('.')[1])
		names[temp1]=temp

# names related to ids: example ==> Adir: id=1,  etc


# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 960) # set video widht
cam.set(4, 720) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)


flag=1
flu=0
start=time.time()
time.clock()
while (True):

    ret, img =cam.read()
    img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
        )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        confi = confidence
        print(confidence)
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence <85):
            tmpID=id
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
#            if (confi  < 70):
            text1 = "This is " + id
            speech1 = Speech(text1, lang)
            #speech.play()
            flag=0
            if tmpID < 3:                
                cwd= os.path.join(os.getcwd(),"/home/pi/Documents/piodT/Blue.py")
                text = "The door is open"
                speech = Speech(text, lang)
            if tmpID > 2 and tmpID < 9:
                cwd= os.path.join(os.getcwd(),"/home/pi/Documents/piodT/Blue.py")
                text="Known person"
                speech = Speech(text, lang)
                #os.system('{} {}'.format('python',cwd))    
            if tmpID > 8: 
                cwd= os.path.join(os.getcwd(),"/home/pi/Documents/piodT/2Lights.py")
                #os.system('{} {}'.format('python',cwd))
                text = "Call 911 and be carefull! This is crime"
                speech = Speech(text, lang)
                #speech.play() 
              
            flu=0
            
        else:
            print(flu)
            if flu!= 2:
                flu+=1 
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                text = "This is " + id
                text1=""
                speech = Speech(text, lang)                
                speech1 = Speech(text1, lang)
                #speech.play()
                flag=0
                cam.release()
                cv2.destroyAllWindows()
                cwd1= os.path.join(os.getcwd(),"/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/01U_face_dataset.py")
                os.system('{} {}'.format('python',cwd1))
                cwd= os.path.join(os.getcwd(),"/home/pi/Documents/piodT/Red.py")
                #os.system('{} {}'.format('python',cwd))
        
            
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  


    
    cv2.imshow('camera',img)  

    
    
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    sec=time.time()-start
    if(sec>=8):
        if(flag==1):
            start=time.time()
            sec=0
        else:
            k=27
    if k == 27:
        tkinter.messagebox.showinfo("Info",text1+"\n"+text)
        os.system('{} {}'.format('python',cwd))
        break




# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
