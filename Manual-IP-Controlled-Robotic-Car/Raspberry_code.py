# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:24:22 2016

@author: pc
"""

import socket, json
import RPi.GPIO as GPIO, sys, time


#use physical pin numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#use pwm on inputs so motors don't go too fast
# Pins 19, 26 Right Motor
# Pins 20, 21 Left Motor
GPIO.setup(19, GPIO.OUT)
p=GPIO.PWM(19, 20)
p.start(0)
GPIO.setup(26, GPIO.OUT)
q=GPIO.PWM(26, 20)
q.start(0)
GPIO.setup(20, GPIO.OUT)
a=GPIO.PWM(20,20)
a.start(0)
GPIO.setup(21, GPIO.OUT)
b=GPIO.PWM(21,20)
b.start(0)

slowspeed = 20
fastspeed = 100

LED1 = 22
LED2 = 18
LED3 = 11
LED4 = 07
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

def reverse():
  p.ChangeDutyCycle(fastspeed)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(fastspeed)
  b.ChangeDutyCycle(0)
  #setLEDs(1, 0, 0, 1)
  #print('straight')

def forwards():
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(fastspeed-1)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(fastspeed)
  #setLEDs(0, 1, 1, 0)
  #print('straight')

def turnright():
  p.ChangeDutyCycle(slowspeed)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(fastspeed)
  #setLEDs(0, 0, 1, 1)
  #print('left')

def turnleft():
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(fastspeed)
  a.ChangeDutyCycle(slowspeed)
  b.ChangeDutyCycle(0)
  #setLEDs(1, 1, 0, 0)
  #print('right')

def stopall():
  p.ChangeDutyCycle(0)
  q.ChangeDutyCycle(0)
  a.ChangeDutyCycle(0)
  b.ChangeDutyCycle(0)
  #setLEDs(1, 1, 1, 1)
  #print('stop')

adr = "localhost"
port = 8001

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((adr,port))


while 1:
	    (data, addr) = s.recvfrom(1024)
	    print "Got >>", str(data)
	    
	    json_data = json.loads(data)
	
	    FB = json_data.get("FB")
	    
	    LR = json_data.get("LR")
	
	    print FB + " " + LR + str(len(FB)) + str(len(LR))
	    if FB == "F":
	         forwards()
	
	    elif FB == "B":
	        reverse()
	
	    elif LR == "L":
	        turnleft()
	
	    elif LR == "R":
	        turnright()
	
	    elif LR == "S" or FB == "S":
	        stopall()

  s.close()
