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
filename2="Test-cycle-"+str(datetime.now())+"Log.csv"  




def write_time(i, current_time, last_time, llast_time):                             
    with open(filename, "a") as log:                  
        log.write("{0},{1}, {2}, {3}\n".format(i,str(current_time),str(last_time),str(llast_time)))
    with open(filename2, "a") as log2:
        if (i%2) != 0 :
            log2.write("{0},{1},{2},{3}\n".format(i,str(current_time),str(last_time),str(llast_time)))
        
try:
    last_time = datetime.now()
    llast_time = datetime.now()
    while True:                               
        if GPIO.input(17) == GPIO.LOW :       
            nowtime=datetime.now()                 
            print i, nowtime, last_time, llast_time                       
            write_time(i, nowtime, last_time, llast_time)
            llast_time = last_time
            last_time = nowtime                 
            i=i+1                             
            sleep(0.3)                        
except KeyboardInterrupt:                     
    print "Exception: KeyboardInterrupt"      

finally:                                      
    GPIO.cleanup()                            
