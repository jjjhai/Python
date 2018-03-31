# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:18:18 2018

@author: Administrator
"""

import threading
import time

var = 0
lock = threading.Lock()
#可重入锁，允许在同一线程中被多次acquire
mutex = threading.RLock()

class MyThread(threading.Thread):
    def __init__(self, num):
        self.num = num
        super(MyThread, self).__init__()
    def run(self):
        lock.acquire()
        print('i am a thread.',self.num)
        lock.release()
        #time.sleep(1)

def run(num):
    print("hi,i am a thread.", num)
    
def main():
    """
    threads = []
    for i in range(5):
        t = threading.Thread(target=run, args=(i,))
        threads.append(t)
        t.start()
    
    for i in threads:
        t.join()
    """

    threads = []
    for i in range(5):
        t = MyThread(i)
        #后台线程
        t.setDaemon(True)
        threads.append(t)
        t.start()
    for i in threads:
        t.join()

        
if __name__=='__main__':
    print('start-->')
    main()
    print('go here-->')
    
    

    

    
    
