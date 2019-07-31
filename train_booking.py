from myutil import Semaphore

import multiprocessing
import time
import sys

pno_base = 121800

available_seats = [i for i in range(1, 10)]

booked_seats = []

semaphore = Semaphore()

def print_seats(seat_state):
    seat_state = [str(x) for x in seat_state]
    print('available seats : ', ' '.join(seat_state))

class Passenger:

    def __init__(self, name):
        global pno_base
        
        global available_seats # shared variable
        global booked_seats # shared variable
        
        self.name = name
        pno_base += 1
        self.pno = pno_base

    def book(self, seatno):
        if available_seats is False:
            print('No seats available.\nPushing into wait queue')
            semaphore.queue.append(self)
            
        elif seatno in available_seats:
            print('seat no.{} booked by passenger {}'.format(
                seatno, self.name))
            remove = available_seats.pop(
                available_seats.index(seatno))
            booked_seats.append(remove)
            
        else:
            print('seat already booked')
            print_seats(available_seats)
            seatno = int(input('New seat for booking : '))
            self.book(seatno)
            
if __name__ == '__main__':
    p1 = Passenger('martin')
    p2 = Passenger('aswathy')

    p1.book(3)
    p2.book(3)
