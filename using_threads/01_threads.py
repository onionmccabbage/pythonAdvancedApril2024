from threading import Thread
import time
import random

# any function may be invoked on a separate thread
def myFn(n):
    '''this is a normal function just like any other'''
    time.sleep( random.random()*2 )#  sleep for 0-2 sec
    print(f'This is the function {n}')

if __name__ == '__main__':
    # we may invoke the function in the normal manner (procedural)
    # myFn()
    # myFn()
    # myFn()
    # we may choose to incvoke any function in a separate thread
    tA = Thread(target=myFn, args=('A',)) # one-member tuple (,)
    tB = Thread(target=myFn, args=('B',))
    tC = Thread(target=myFn, args=('C',))
    print('on the mainthread')
    tA.start() # at this point the function will start execution on a separate thread
    tB.start() # the threads run concurrently
    tC.start() # by now we have FOUR threads - the main one and these three extras
    # by default our threads are not blocking the main thread
    tA.join() # if we choose to join, then the main thread will wait until the other thread (re)joins
    tB.join()
    tC.join()
    print('still on the main thread')