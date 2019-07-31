'''Understanding OS topic Semaphore
using train-ticket booking program.

The primary shared variable is the seatno
No two process (Passenger booking) should
access the same seatno simultaneosly'''

from myutil import CountingSemaphore
from myutil import UP, DOWN
from multiprocessing import Pool 

import time
import sys

pno_base = 121800

available_seats = [i for i in range(1, 10)]
n = len(available_seats)

booked_seats = []

semaphore = CountingSemaphore(n)

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

        self.myseat = None

    def book(self, seatno):
        '''Booking the tickets is like
performing DOWN or P(S) then
selecting the seats (critical section) and then
performing an UP or V(S). The main shared variable
in this design is the seatno.'''

        # changes required
        DOWN(semaphore, self.book, seatno)
        
        if len(available_seats) == 0:
            print('''No seats available.
                  You are pushed to wait-Queue''')
            
        elif seatno in available_seats:
            print('seat no.{} booked by passenger {}'.format(
                seatno, self.name))
            booked = available_seats.pop(
                available_seats.index(seatno))

            self.myseat = booked
            
            booked_seats.append(booked)
            
        else:
            print('seat already booked')
            print_seats(available_seats)
            seatno = int(input('New seat for booking : '))
            self.book(seatno)

    def cancel(self):
        cindex = booked_seats.index(self.myseat)
        canceled = booked_seats.pop(cindex)

        print('Your ticket has been canceled')

        available_seats.insert(canceled - 1, canceled)

        # changes required
        UP(semaphore)
        
            
if __name__ == '__main__':
    p1 = Passenger('martin')
    p2 = Passenger('aswathy')

    p1.book(3)
    p2.book(3)

    p1.cancel()

    print(available_seats)

