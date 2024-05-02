import threading
import time
import random
import timeit

ticketsAvailable = 100

class TicketSeller(threading.Thread):
    '''this class will sell tickets'''
    ticketsSold = 0
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.__lock = lock
        print('Ticket seller starts selling tickets')
    def run(self):
        global ticketsAvailable
        running = True
        while running:
            self.randomDelay() # hang about ...
            self.__lock.acquire()
            if ticketsAvailable <=0:
                running = False
            else:
                ticketsAvailable -= 1
                self.ticketsSold += 1
                print(f'Sold a ticket: {ticketsAvailable} remaining')
            self.__lock.release()
        print(f'Sold {self.ticketsSold}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.75, 1

def main():
    '''invoke several ticket sellers on threads'''
    lock = threading.Lock()
    sellers_l = []
    start = timeit.default_timer()
    for _ in range(0, 8):
        seller = TicketSeller(lock)
        sellers_l.append(seller)
        seller.start()
    for seller in sellers_l:
        seller.join()
    end = timeit.default_timer()
    print(f'total time: {end-start}')

if __name__ == '__main__':
    main()