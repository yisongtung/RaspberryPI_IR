import RPi.GPIO as GPIO
import time
photo1=15
photo2=13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(photo1,GPIO.IN)
GPIO.setup(photo2,GPIO.IN)
while(1):
    print(GPIO.input(photo1))
    time.sleep(0.01)
