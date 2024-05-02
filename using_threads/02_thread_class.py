from threading import Thread
import time
import random

class MyClass(Thread):
    '''Any class may be invoked as a thread, but it is easiest if the class inherists from Thread'''
    def __init__(self, n):
        Thread.__init__(self) # we call the __init__ of the parent class
        self.n = n # we could use property get/set methods
    def run(self):
        '''When this class is invoked the run method will be executed'''
        for i in range(0,10): # on average this should take 0.5 sec
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1) # sleep for up to 1/10 sec

def main():
    '''we can invoke our class as a thread'''
    print('on the main thread')
    tA = MyClass('A') # we have access to a new thread
    tA.start()
    print('still on the main thread')


if __name__ == '__main__':
    main()
