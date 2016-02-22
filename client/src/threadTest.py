# http://www.jb51.net/article/57672.htm

from threading import Lock, Thread, currentThread
import time


num = 0
lock = Lock()
 
def func(st):
    global num
    print (currentThread().getName() + ' try to acquire the lock')
    if lock.acquire():
        print (currentThread().getName() + ' acquire the lock.' )
        print (currentThread().getName() +" :%s" % str(num) )
        num += 1
        time.sleep(st)
        print (currentThread().getName() + ' release the lock.'  )       
        lock.release()
 
t1 = Thread(target=func, args=(8,))
t2 = Thread(target=func, args=(4,))
t3 = Thread(target=func, args=(2,))
t1.start()
t2.start()
t3.start()