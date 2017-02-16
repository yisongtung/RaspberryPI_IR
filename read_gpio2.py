import RPi.GPIO as GPIO
import time
photo1=11
photo2=13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(photo1,GPIO.IN)
GPIO.setup(photo2,GPIO.IN)
while(1):
    print('start')
    while(GPIO.input(photo1)):
        pass
    t1=time.time()*1000
    while(not GPIO.input(photo1)):
        pass
    while(GPIO.input(photo2)):
        pass
    t2=time.time()*1000    
    while(not GPIO.input(photo2)):
        pass
    print(t2-t1)
