
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
GPIO.setup(17,GPIO.IN)

sensorState=GPIO.LOW
lastState=GPIO.LOW

while True:
 
    if GPIO.input(17)==GPIO.HIGH :
        sensorState=GPIO.HIGH
    else :
        sensorState=GPIO.LOW
    #sensorState=GPIO.input(17)

    if sensorState==GPIO.LOW :
        GPIO.output(27,GPIO.HIGH)
    else :
        GPIO.output(27,GPIO.LOW)
    if (sensorState and (not lastState)) :
        print("Unbroken")
    if ((not sensorState) and lastState) :
        print("Broken")
        print datetime.now()
    #else :
        #print ("Unbroken")
    #time.sleep(0.2)
    lastState=sensorState

