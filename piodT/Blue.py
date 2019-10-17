#!/usr/bin/env python
import time
import pigpio
 #connect to local pi
pi2=pigpio.pi()

h=3

pi2.set_mode(h,pigpio.OUTPUT)
pi2.write(h,0)
pi2.write(h,1)
time.sleep(5)
	
pi2.write(h,0)
pi2.stop()


