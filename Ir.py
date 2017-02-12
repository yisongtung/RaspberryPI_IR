import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.IN)

    #I've tried with and without pull pu, i.e., pull_up_down = ~
    ##GPIO.PUD_UP
while True:
    if(GPIO.input(17) ==1):
        print("Beam Broken")
    if(GPIO.input(17) ==0):
        print("Solid")
    time.sleep(0.3)
    #I've also looked at print(GPIO.input(17))
