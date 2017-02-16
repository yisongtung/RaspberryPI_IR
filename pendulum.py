import RPi.GPIO as GPIO #Lib for controling GPIO pins
import time # Lib for time.time() and time.sleep()

photo1=11 
photo2=11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(photo1,GPIO.IN)
GPIO.setup(photo2,GPIO.IN)

while(GPIO.input(photo1)): #wait until first pass
        pass
last=time.time() #set current time
time.sleep(0.1) #small delay
tmp=0
while(1): #loop forever(stop by pressing ctrl+c)
    while(GPIO.input(photo1)):#wait until next pass
        pass 
    t=time.time()*1000 #get current time    
    if tmp==0:
        tmp=t-last
        print(t-last) #print delta time
    else:
        print(t-last,tmp+t-last) #print delta time
        tmp=0
    last=t #set 'last' as curent time 
    time.sleep(0.1) #small delay

