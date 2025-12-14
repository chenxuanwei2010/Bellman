import time
import os
file = "d:/Users/seewo/Desktop/clock.mp3"

while 1:
    t = time.localtime(time.time())
    if t.tm_hour == 8 and t.tm_min == 15 and t.tm_sec == 0:
        os.system(file)
        time.sleep(1)
    elif t.tm_hour == 10 and t.tm_min == 10 and t.tm_sec == 0:
        os.system(file)
        time.sleep(1)
        
        
    elif t.tm_hour == 13 and t.tm_min == 55 and t.tm_sec == 0:
        os.system(file)
        time.sleep(1)
    elif t.tm_hour == 14 and t.tm_min == 55 and t.tm_sec == 0:
        os.system(file)
        time.sleep(1)
    elif t.tm_hour == 15 and t.tm_min == 45 and t.tm_sec == 0:
        os.system(file)
        time.sleep(1)
    elif t.tm_hour == 18 and t.tm_min == 55 and t.tm_sec == 0:
        os.system(file)
        time.sleep(1)
    elif t.tm_hour == 20 and t.tm_min == 5 and t.tm_sec == 0:
        os.system(file)
        time.sleep(1)
    elif t.tm_hour == 9 and t.tm_min == 50:

        time.sleep(1)
    elif t.tm_hour == 11 and t.tm_min == 30:
        
        time.sleep(1)
    elif t.tm_hour == 14 and t.tm_min == 45:
        
        time.sleep(1)
    elif t.tm_hour == 15 and t.tm_min == 40:
      
        time.sleep(1)
    elif t.tm_hour == 16 and t.tm_min == 35:
       
        time.sleep(1)
    elif t.tm_hour == 20 and t.tm_min == 0:

        time.sleep(1)
    elif t.tm_hour == 20 and t.tm_min == 35:
        time.sleep(1)
    else:
        time.sleep(1)
