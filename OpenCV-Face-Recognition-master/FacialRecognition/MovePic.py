import os
import shutil


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
path_DS="/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"

array2=arr.array ('i',[-1,0,0,0,0,0,0,0,0,0,0])
# For each person, enter one numeric face id

def countFile(typeID):
    array=arr.array ('i',[-1,0,0,0,0,0,0,0,0,0,0])
    temp=""
    for root,dirs,files in os.walk("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"):
        for filename in files:
            temp=filename.split('.')[1]
            temp1=int(temp)
            array[temp1]=1   
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



while True:    
    face_id = input('\n press 1 to add person to the super list \n press 2 to add person the white list\n press 3 to add person to the black list \npress 4 to exit')
    print(face_id)
    Error=countFile(int(face_id))
    print(Error)
    if(Error==99):
        print("The list you choosed is full")
    elif face_id==4:
        exit()    
    else:
        Name=input("\n Enter your name")
        array2[Error]=1
        break
#for x in range(1,11):
#	print (str(x)+ "----" + str(array[x]))
     
face_id=Error
os.rename("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/datasetU/unknown.1.0.1.jpg","/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset/"+Name+".1.0.1.jpg")
#shutil.move("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/datasetU/unknown.1.0.1.jpg","/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset/unknown.1.0.1.jpg")
