import RPi.GPIO as GPIO             #�ޥ�GPIO�}��
import time                         #�ޥήɶ��Ҳ�
from time import sleep              #�ޥμȰ��Ҳ�
from datetime import datetime       #�ޥΤ���ɶ��Ҳ�
import os                           #�ޥΨt�μҲ�

GPIO.setmode(GPIO.BCM)              #�]�wGPIO�}��覡
GPIO.setup(17, GPIO.IN)             #�]�wGPIO 17�}�쬰��J�Ҧ��AŪ���������
GPIO.setup(27, GPIO.OUT)            #�]�wGPIO 27�}�쬰��X�Ҧ�

i=1                                 #�O����������
filename="Test-"+str(datetime.now())+"Log.csv"        #�O���ɮשR�W

def write_time(i, Time1):                             #�Ƶ{���G�O�������ɶ�
    with open(filename, "a") as log:                  #�}�ҰO����
        log.write("{0},{1}\n".format(i,str(Time1)))   #�O�������ɶ�
try:                                          #�Ҧp�ƥ�B�z try�K.  except �K...finally �K...�A�קK�{�������`���       
    while True:                               #�O���ɶ��j��
        if GPIO.input(17) == GPIO.LOW :       #Ū�����~�u�B�_�A�P�_LOW�C�q���o��
            dt=datetime.now()                 #Ū���ɶ�
            print i, dt                       #�ù��V�ܰ������Ƥήɶ�
            write_time(i, dt)                 #�I�s�Ƶ{��(�O�������ɶ�))
            i=i+1                             #�ܼ�i�[1
            sleep(0.3)                        #�Ȱ�0.3��
except KeyboardInterrupt:                     #�ҥ~�o�ͳB�z
    print "Exception: KeyboardInterrupt"      #��L���_�{������u�@-�ù���ܤ��_�T��

finally:                                      
    GPIO.cleanup()                            #�{�������A�M��GPIO�}��T����
