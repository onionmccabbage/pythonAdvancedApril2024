import time
import random

# any function may be invoked on a separate thread
def myFn():
    '''this is a normal function just like any other'''
    time.sleep( random.random()*2 )#  sleep for 0-2 sec
    print(f'This is the function')

if __name__ == '__main__':
    # we may invoke the function in the normal manner
    myFn()
    myFn()
    myFn()
