#!/usr/bin/env python
import time
import pigpio
import RPi.GPIO as GPIO
import os


B=26

GPIO.setmode(GPIO.BCM)

GPIO.setup(B,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
	if GPIO.input(26):
		i=2
	else:
		path="/home/pi/Documents/OpenCV-Face-Recognition-master/FacialRecognition/03_face_recognition.py"
		cwd= os.path.join(os.getcwd(),path)
		os.system('{} {}'.format('python',cwd))
		time.sleep(0.5)
		break


