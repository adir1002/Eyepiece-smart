#!/usr/bin/env python
import time
import pigpio
import RPi.GPIO as GPIO
l=2
B=26
pi=pigpio.pi()
pi.set_mode(l,pigpio.OUTPUT)
pi.write(l,0)
GPIO.setmode(GPIO.BCM)

GPIO.setup(B,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(26):
		i=2
	else:
		pi.write(l,1)
		print("wow")
		time.sleep(0.5)
	pi.write(l,0)

pi.stop()
	


