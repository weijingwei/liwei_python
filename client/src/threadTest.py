# http://www.jb51.net/article/57672.htm

from threading import Lock, Thread, currentThread
import time


num = 0
lock = Lock()
class Test(object):
    def func(self, st, hi):
        global num
        print (currentThread().getName() + ' try to acquire the lock')
        if lock.acquire():
            print (currentThread().getName() + ' acquire the lock.', hi[0] )
            print (currentThread().getName() +" :%s" % str(num) )
            num += 1
            time.sleep(st)
            print (currentThread().getName() + ' release the lock.'  )       
            lock.release()
            
    def readFile(self, params):
        print(params[1])
 
if __name__ == '__main__':
#     func = Test().func
#     t1 = Thread(target=func, args=(8, ("h1",)))
#     t2 = Thread(target=func, args=(4, ("h2",)))
#     t3 = Thread(target=func, args=(2, ("h3",)))
#     t1.start()
#     t2.start()
#     t3.start()
    for line in open("C:/Users/IBM_ADMIN/Desktop/Log/lis_translator_in_1_20160219_171713.log"):
        Thread(target=Test().readFile, args=(("line", (line,)),)).start()