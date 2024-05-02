import threading

counter = 1 # here is a global asset (could be some large resource we share)

def workerA():
    '''this worker will acess the global counter to increment by 1 up to 10'''
    global counter
    while counter <10:
        counter += 1
        print('Worker A incrememnts to {counter}')

def workerB():
    '''this worker will acess the global counter to deccrement by 1 down to -10'''
    global counter
    while counter >-10:
        counter -= 1
        print('Worker B decrememnts to {counter}')

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