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
filename3="Test-Cycle-"+str(datetime.now())+"Log-dt.csv"


def write_time(i, current_time, last_time, llast_time):                             
    with open(filename, "a") as log:                  
        log.write("{0},{1}, {2}, {3}\n".format(i,str(current_time),str(last_time),str(llast_time)))
    with open(filename2, "a") as log2:
        if (i%2) != 0 :
            log2.write("{0},{1},{2},{3}\n".format(i,str(current_time),str(last_time),str(llast_time)))
    with open(filename3, "a") as log3:
        if (i%2) != 0 :
            dt1 = current_time - llast_time
            print dt1.total_seconds()
            log3.write("{0},{1}\n".format(i/2+1,str(dt1.total_seconds())))        
        
try:
    last_time = datetime.now()
    llast_time = datetime.now()
    times = input("How many times:")
    print times
    while True:                               
        if GPIO.input(17) == GPIO.LOW :       
            nowtime=datetime.now()                 
            print i, nowtime, last_time, llast_time                       
            write_time(i, nowtime, last_time, llast_time)
            llast_time = last_time
            last_time = nowtime
            dt = nowtime - llast_time
            #print dt.total_seconds()                  
            i=i+1                             
            sleep(0.3)                        
except KeyboardInterrupt:                     
    print "Exception: KeyboardInterrupt"      

finally:                                      
    GPIO.cleanup()                            
