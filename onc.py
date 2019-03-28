#import signal
#def timeout_handler(signal, frame):
#    raise Exception('Time is up!')
#signal.signal(signal.SIGALRM, timeout_handler)
def Kliker()
import sys
import select
import msvcrt 
import time
chek = True
while chek:
    print("Накликайте 30 раз чтобы разбудить спящую обезбяну")
    start = time.time()
    x = []
    PERIOD_OF_TIME = 5 # 5min
    y=0
    while True :
        if time.time() > start + PERIOD_OF_TIME : break
        ret = msvcrt.getch()
        x.append(ret)
           
    print(len(x))
    if len(x)>30:
        chek=False 
        print("Вы разбудили древнее зло")