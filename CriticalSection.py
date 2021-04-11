import threading
import time

class CriticalSection():
    def __init__(self):
        self.sem = threading.Semaphore()
        
    def processs_1(self):
        while True:
            print("Entrey Section 1")
            self.sem.acquire()
            self.criticalsection()
            self.sem.release()
            print("Critical Section over for process 1")
            time.sleep(3)
        
    def processs_2(self):
        while True:
            print("Entrey Section 2")
            self.sem.acquire()
            self.criticalsection()
            self.sem.release()
            print("Critical Section over for process 2")
            time.sleep(3)
        
    def criticalsection(self):
        print("Entered Critical Section. Perform operation an shared resource")
        
    def main(self):
        t1 = threading.Thread(target = self.process_1)
        t1.start()
        t2 = threading.Thread(target = self.process_2)
        t2.start()
        

if __name__ == "__main__":
    c = CriticalSection()
    c.main()