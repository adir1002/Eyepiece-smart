import os 
import array as arr

array= ['NULL','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE','NONE']

temp=''
for root,dirs,files in os.walk("/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/dataset"):
	for filename in files:
		temp=filename.split('.')[0]
		temp1=int(filename.split('.')[1])
		array[temp1]=temp

for x in range(0,11):
	print (str(x)+ "----" + str(array[x]))

