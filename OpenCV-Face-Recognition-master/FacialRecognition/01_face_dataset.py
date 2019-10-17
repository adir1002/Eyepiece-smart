
import cv2
import os
import array as arr


cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

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
        cv2.imwrite("dataset/"+Name+"." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

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


