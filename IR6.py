import RPi.GPIO as GPIO             
import time                         
from time import sleep              
from datetime import datetime       
import os                           

GPIO.setmode(GPIO.BCM)              
GPIO.setup(17, GPIO.IN)             
GPIO.setup(27, GPIO.OUT)            

i=1                                 
filename="Test-"+str(datetime.now())+"Log.csv"        

def write_time(i, Time1):                             
    with open(filename, "a") as log:                  
        log.write("{0},{1}\n".format(i,str(Time1)))   
try:                                          
    while True:                               
        if GPIO.input(17) == GPIO.LOW :       
            dt=datetime.now()                 
            print i, dt                       
            write_time(i, dt)                 
            i=i+1                             
            sleep(0.3)                        
except KeyboardInterrupt:                     
    print "Exception: KeyboardInterrupt"      

finally:                                      
    GPIO.cleanup()                            
