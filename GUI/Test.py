from tkinter import *
from tkinter import simpledialog 
import tkinter.messagebox
import tkinter
import os
import cv2
from time import sleep
from picamera import PiCamera
from PIL import ImageTk,Image
import array as arr
import numpy as np
import time
import pigpio
import RPi.GPIO as GPIO


#camera=PiCamera()


B=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(B,GPIO.IN,pull_up_down=GPIO.PUD_UP)

top=Tk()
top.geometry('450x550')
top.title("EYEPISMART")
top.configure(background="powder blue")
img=PhotoImage(file="/home/pi/Documents/ICON150x50.png")
panel=tkinter.Label(top,image=img)
panel.image=img
panel.pack()
panel.place(bordermode=OUTSIDE,x=150,y=450)


def PushButton():
	print("234523452")
	

def DelPer(B1,B3):
	i=0
	
	Nameslist=[]
	temp=""
	for root,dirs,files in os.walk("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"):
		for filename in files:
			temp=filename.split('.')[0]
			if(temp not in Nameslist):				
				Nameslist.append(temp)	
	if(len(Nameslist)==0):
		#close halonit
		tkinter.messagebox.showinfo("Info","The dataset is empty")
	else:
		top_del=Tk()

		top_del.geometry('600x400')
		top_del.title("Delete a person")
		top_del.configure(background="powder blue")

		BtnList=[]
		for name in Nameslist:
			BtnList.append(Button(top_del,text=name,command= lambda: Del_SpecificUsr(name,B1,B3)))
		for btn in BtnList:
			btn.pack()
			btn.place(bordermode=OUTSIDE,height=40,width=200,x=125,y=30+i)
			i+=50
	if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == True):
		B1["state"] ="normal"
		B2["state"] ="normal"
	if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == False):
		B1["state"] ="disabled"
		B2["state"] ="disabled"

def Del_SpecificUsr(name,B1,B3):
	for root,dirs,files in os.walk("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"):
		for filename in files:
			temp=filename.split('.')[0]
			if(temp==name):
				os.remove('/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset/'+filename)	
	tkinter.messagebox.showinfo("Info","The person was deleted from dataset")
	flag=0
	for root,dirs,files in os.walk("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"):
		for filename in files:
			flag=flag+1
	if(flag>0):
		Playtrainer()
	else:
		if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == True):
			os.remove("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml")		
			B1["state"] ="disabled"
			B3["state"] ="disabled"
			


def countFile(typeID):
    array=arr.array ('i',[-1,0,0,0,0,0,0,0,0,0,0])
    temp=""
    for root,dirs,files in os.walk("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"):
        for filename in files:
            temp=filename.split('.')[1]
            temp1=int(temp)
            array[temp1]=1
#    for x in range(1,11):
#        print (str(x)+ "----" + str(array[x]))    
    if typeID==1:        
        if array[1]==0:
            return 1
        elif array[2]==0:
            return 2
        else:
            return 99
    elif typeID==2:
        if array[3]==0:
            return 3
        elif array[4]==0:
            return 4
        elif array[5]==0:
            return 5
        elif array[6]==0:
            return 6
        elif array[7]==0:
            return 7
        elif array[8]==0:
            return 8
        else:
            return 99
    elif typeID==3:
        if array[9]==0:
            return 9
        elif array[10]==0:
            return 10
        else:
            return 99  

def hello():
	tkinter.messagebox.showinfo("top","indasdasdfafsadasdadsasdasdasd")
	
def start_recog():
	if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == True):
		path="/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/03_face_recognitiongibuy.py"
		cwd= os.path.join(os.getcwd(),path)
		os.system('{} {}'.format('python',cwd))

def NewPer(B5,B6):
	top=Tk()
	top.geometry('600x400')
	top.title("Add a new person")
	top.configure(background="powder blue")
	
	B1=Button(top,text="Super user",command=lambda:AddSup(B5,B6))
	B1.pack()
	B1.place(bordermode=OUTSIDE,height=40,width=200,x=200,y=30)

	B2=Button(top,text="White list",command=lambda:AddWhi(B5,B6))
	B2.pack()
	B2.place(bordermode=OUTSIDE,height=40,width=200,x=200,y=80)

	B3=Button(top,text="Black list",command=lambda:AddBla(B5,B6))
	B3.pack()
	B3.place(bordermode=OUTSIDE,height=40,width=200,x=200,y=130)
	top.mainloop()

def getImagesAndLabels(path):
	detector = cv2.CascadeClassifier("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/haarcascade_frontalface_default.xml");
	imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
	faceSamples=[]
	ids = []

	for imagePath in imagePaths:

		PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
		img_numpy = np.array(PIL_img,'uint8')

		id = int(os.path.split(imagePath)[-1].split(".")[1])
		faces = detector.detectMultiScale(img_numpy)

		for (x,y,w,h) in faces:
			faceSamples.append(img_numpy[y:y+h,x:x+w])
			ids.append(id)

	return faceSamples,ids

def Playtrainer():
	# Path for face image database
	path = '/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset'

	recognizer = cv2.face.LBPHFaceRecognizer_create()
	

	# function to get the images and label data

	print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
	faces,ids = getImagesAndLabels(path)
	recognizer.train(faces, np.array(ids))

	# Save the model into trainer/trainer.yml
	recognizer.write('/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

	# Print the numer of faces trained and end program
	print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

def AddSup(B1,B3):
	flag=countFile(1)
	if(flag==99):
		tkinter.messagebox.showinfo("top","The list you choosed is full")
	else:
		name=simpledialog.askstring("Add a Super user","Enter a name")
		AddNew(name,flag,B1,B3)
	
def AddWhi(B1,B3):
	flag=countFile(2)
	if(flag==99):
		tkinter.messagebox.showinfo("top","The list you choosed is full")
	else:
		name=simpledialog.askstring("Add a White user","Enter a name")
		AddNew(name,flag,B1,B3)
	

def AddBla(B1,B3):
	flag=countFile(3)
	if(flag==99):
		tkinter.messagebox.showinfo("top","The list you choosed is full")
	else:
		name=simpledialog.askstring("Add a Black user","Enter a name")
		AddNew(name,flag,B1,B3)	

def AddNew(Name,face_id,B1,B3):    
	cam = cv2.VideoCapture(0)
	cam.set(3, 640) # set video width
	cam.set(4, 480) # set video height
	face_detector = cv2.CascadeClassifier('/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/haarcascade_frontalface_default.xml')
	path_DS="/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"
	print("\n [INFO] Initializing face capture. Look the camera and wait ...")
	# Initialize individual sampling face count
	count = 0

	while(True):
		ret, img = cam.read()
		img = cv2.flip(img, -1) # flip video image vertically
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_detector.detectMultiScale(gray, 1.3, 5)

		for (x,y,w,h) in faces:

			cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
			count += 1

			# Save the captured image into the datasets folder
			cv2.imwrite("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset/"+Name+"." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

			cv2.imshow('image', img)

		k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
		if k == 27:
			break
		elif count >= 30: # Take 30 face sample and stop video
			 break

	# Do a bit of cleanup
	print("\n [INFO] Exiting Program and cleanup stuff")
	cam.release()
	cv2.destroyAllWindows()
	Playtrainer()
	tkinter.messagebox.showinfo("Info","The person was added to the dataset")
	if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == True):
		B1["state"] ="normal"
		B3["state"] ="normal"
	if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == False):
		B1["state"] ="disabled"
		B3["state"] ="disabled"
	

def opencame():
	camera=PiCamera()
	camera.rotation=180
	camera.start_preview()
	sleep(7)
	camera.stop_preview()

def recordvideo():
	camera=PiCamera()
	camera.rotation=180
	camera.start_preview()
	camera.start_recording('/home/pi/video.h264')
	sleep(5)
	camera.stop_recording()
	camera.stop_preview()


def countFileU():
    i=0
    for root,dirs,files in os.walk("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/datasetU"):
        for filename in files:
                i=i+1
    i=i/30
    return (i+1)
    
def CheckUdataset1(num):
	
	
	top_Udb=Tk()
	top_Udb.geometry('600x400')
	top_Udb.title("Unknown list")
	top_Udb.configure(background="powder blue")
	
#	for x in range(int(num)):
#		x=x+1
#	panel = tkinter.Label(top_Udb,image=ImageTk.PhotoImage(Image.open("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/datasetU/unknown.1.1.jpg")))
	im=Image.open("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/datasetU/unknown.1.1.jpg")
	im.save("unknown.1.1.png")
	img=PhotoImage(im)
	panel=tkinter.Label(top_Udb,image=img)
	panel.image=img
	panel.pack()
	panel.place(bordermode=OUTSIDE,x=150,y=450)			
	top=Tk()

def CheckUdataset(num):	
	top1=Tk()
	top1.geometry('450x550')
	top1.title("EYEPISMART")
	top1.configure(background="powder blue")
	im=Image.open("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/datasetU/unknown.1.1.jpg")
	im.save("unknown.1.1.png")
	img=PhotoImage(im)
	print("11111111111111111111112121")
	#img=PhotoImage(file="/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/datasetU/unknown.1.1.jpg")
	panel1=tkinter.Label(top1,image=img)
	panel1.image=img
	panel1.pack()
	panel1.place(bordermode=OUTSIDE,x=150,y=450)
	

B1=Button(top,text="Face recognition",command=start_recog)
B1.pack()
B1.place(bordermode=OUTSIDE,height=40,width=200,x=125,y=30)
if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == False):
		B1["state"] ="disabled"
if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == True):
		B1["state"] ="normal"

B3=Button(top,text="Delete a person",command=lambda:DelPer(B1,B3))
B3.pack()
B3.place(bordermode=OUTSIDE,height=40,width=200,x=125,y=130)
if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == False):
		B3["state"] ="disabled"
if(os.path.isfile("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/trainer/trainer.yml") == True):
		B3["state"] ="normal"

B2=Button(top,text="Add a new person",command=lambda:NewPer(B1,B3))
B2.pack()
B2.place(bordermode=OUTSIDE,height=40,width=200,x=125,y=80)

B4=Button(top,text="Check the unknown list",command=lambda: CheckUdataset(countFileU()))
B4.pack()
B4.place(bordermode=OUTSIDE,height=40,width=200,x=125,y=180)

B5=Button(top,text="Open camera",command=opencame)
B5.pack()
B5.place(bordermode=OUTSIDE,height=40,width=200,x=125,y=230)

B6=Button(top,text="Save video live",command=recordvideo)
B6.pack()
B6.place(bordermode=OUTSIDE,height=40,width=200,x=125,y=280)

B6=Button(top,text="Sleep mode",command=img)
B6.pack()
B6.place(bordermode=OUTSIDE,height=40,width=200,x=125,y=330)

GPIO.add_event_detect(26,GPIO.RISING,PushButton)

top.mainloop()



