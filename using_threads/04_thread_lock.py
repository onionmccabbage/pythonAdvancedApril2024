import threading

counter = 1 # here is a global asset (could be some large resource we share)
lock = threading.Lock()

def workerA():
    '''this worker will acess the global counter to increment by 1 up to 10'''
    global counter
    lock.acquire() #we have exclusive access to the lock
    while counter <10:
        counter += 1
        print(f'Worker A incrememnts to {counter}')
    lock.release()

def workerB():
    '''this worker will acess the global counter to deccrement by 1 down to -10'''
    global counter
    lock.acquire() #we have exclusive access to the lock
    while counter >-10:
        counter -= 1
        print(f'Worker B decrememnts to {counter}')
    lock.release()

def main():
    '''invoke the workers as threads'''
    t1 = threading.Thread(target=workerA) 
    t2 = threading.Thread(target=workerB) 
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()