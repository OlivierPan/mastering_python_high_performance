from threading import Thread
import time
import threading


global_value = 0

def run(threadName):
    global global_value
    local_cp = global_value
    print(f"{threadName} with value {local_cp}")
    global_value = local_cp+1

def run2(threadName, lock):
    global global_value
    lock.acquire()
    local_cp = global_value
    print(f"{threadName} with value {local_cp}")
    global_value +=1
    lock.release()

lock = threading.Lock()

for i in range(10):
    Thread(target=run2, args=("Thread-"+str(i),lock, )).start()

while 1:
    pass