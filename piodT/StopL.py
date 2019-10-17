#!/usr/bin/env python

import pigpio
pi=pigpio.pi()
pi2=pigpio.pi()  #connect to local pi

g=3

pi.set_mode(g,pigpio.OUTPUT)
pi.write(g,0)
pi.stop()

g=2
pi2.set_mode(g,pigpio.OUTPUT)
pi2.write(g,0)
pi2.stop()

