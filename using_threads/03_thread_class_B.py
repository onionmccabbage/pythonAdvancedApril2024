from threading import Thread
import time
import random

class MyClassB(): # we do not have to inherit from Thread
    '''To call a class as a thread we must declare a __call__ method'''
    def __init__(self):
        pass
        # self.n = n # we could use property get/set methods

    def __call__(self, n): # we may choose to pass argumetns to __call__
        '''__call__ lets us invoke this on a thread'''
        msg = ''
        for i in range(0,10): # on average this should take 0.5 sec
            msg += f'{n} is sleeping\n'
            time.sleep(random.random()*0.1) # sleep for up to 1/10 sec
        print(msg, end='') # try to minimize I/O

def main():
    '''we can invoke our class as a thread'''
    cA = MyClassB() # we have access to a new class instance
    print('on the main thread')
    thread_l = []
    for _ in range(0,8):
        thread_l.append(Thread(target=cA, args=(_,)))
    print(f'Main thread has spawned several child threads')
    for item in thread_l:
        item.start()
    for item in thread_l:
        item.join()

    print('still on the main thread')


if __name__ == '__main__':
    main()

