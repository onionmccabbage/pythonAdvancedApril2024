import threading

counter = 1 # here is a global asset (could be some large resource we share)
lock = threading.Lock()

def workerA():
    '''this worker will acess the global counter to increment by 1 up to 10'''
    global counter
    lock.acquire() #we have exclusive access to the lock
    try:
        while counter <10:
            counter += 1
            print(f'Worker A incrememnts to {counter}')
    except Exception as err:
        print(err)
    finally:
        if lock:
            lock.release()

def workerB():
    '''this worker will acess the global counter to deccrement by 1 down to -10'''
    global counter
    lock.acquire() #we have exclusive access to the lock
    try:
        while counter >-10:
            counter -= 1
            print(f'Worker B decrememnts to {counter}')
    except Exception as err:
        print(err)
    finally:
        if lock:
            lock.release()

def main():
    '''invoke the workers as threads'''
    t1 = threading.Thread(target=workerA) 
    t2 = threading.Thread(target=workerB) 
    t1.start() # whichever thread gets in first will ahave exclusive access to the lock
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()