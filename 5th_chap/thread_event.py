import threading
import time

class ThreadA(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.event = event

    def run(self):
        count = 0
        while count <5:
            time.sleep(1)
            if self.event.is_set():
                print("Thread A")
                self.event.clear() # the event is taken care of
            count +=1

class ThreadB(threading.Thread):
    def __init__(self,event):
        threading.Thread.__init__(self)
        self.event = event
    def run(self):
        count =0
        while count <5:
            time.sleep(1)
            if not self.event.is_set():
                print("THREAD B")
                self.event.set()# set but has no info
            count+=1
event = threading.Event()
ta = ThreadA(event)
tb = ThreadB(event)

ta.start()
tb.start()