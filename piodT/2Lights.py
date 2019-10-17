#!/usr/bin/env python
import time
import pigpio
pi=pigpio.pi() #connect to local pi
pi2=pigpio.pi()

g=2
h=3
i=0

pi.set_mode(g,pigpio.OUTPUT)
pi.write(g,0)
pi2.set_mode(h,pigpio.OUTPUT)
pi2.write(h,0)
while i<=5:
	if pi.read(h):
		pi.write(g,1)
		pi2.write(h,0)
		i=i+1
		time.sleep(0.5)
	else :
		pi.write(g,0)
		pi2.write(h,1)
		time.sleep(0.5)
	
pi.write(g,0)
pi2.write(h,0)
pi.stop()
pi2.stop()

