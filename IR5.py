import RPi.GPIO as GPIO             #引用GPIO腳位
import time                         #引用時間模組
from time import sleep              #引用暫停模組
from datetime import datetime       #引用日期時間模組
import os                           #引用系統模組

GPIO.setmode(GPIO.BCM)              #設定GPIO腳位方式
GPIO.setup(17, GPIO.IN)             #設定GPIO 17腳位為輸入模式，讀取偵測資料
GPIO.setup(27, GPIO.OUT)            #設定GPIO 27腳位為輸出模式

i=1                                 #記錄偵測次數
filename="Test-"+str(datetime.now())+"Log.csv"        #記錄檔案命名

def write_time(i, Time1):                             #副程式：記錄偵測時間
    with open(filename, "a") as log:                  #開啟記錄檔
        log.write("{0},{1}\n".format(i,str(Time1)))   #記錄偵測時間
try:                                          #例如事件處理 try….  except …...finally …...，避免程式不正常當機       
    while True:                               #記錄時間迴圈
        if GPIO.input(17) == GPIO.LOW :       #讀取紅外線遮斷，判斷LOW低電壓發生
            dt=datetime.now()                 #讀取時間
            print i, dt                       #螢幕顥示偵測次數及時間
            write_time(i, dt)                 #呼叫副程式(記錄偵測時間))
            i=i+1                             #變數i加1
            sleep(0.3)                        #暫停0.3秒
except KeyboardInterrupt:                     #例外發生處理
    print "Exception: KeyboardInterrupt"      #鍵盤中斷程式執行工作-螢幕顯示中斷訊息

finally:                                      
    GPIO.cleanup()                            #程式結束，清除GPIO腳位訊號值
