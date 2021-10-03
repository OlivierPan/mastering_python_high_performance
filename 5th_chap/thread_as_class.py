import threading
import time

class MyThread(threading.Thread):

    def __init__(self, count):
        threading.Thread.__init__(self)
        self.total = count
    def run(self):
        for i in range(self.total):
            time.sleep(1)
            print(f"Thread: {self.name} -- {i}")

t = MyThread(4)
t2 = MyThread(3)

t.start()
t2.start()
# t.join()
# t2.join()

print("PROGRAME IS OK")