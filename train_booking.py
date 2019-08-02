'''Understanding OS topic Semaphore
using train-ticket booking program.

The primary shared variable is the seatno
No two process (Passenger booking) should
access the same seatno simultaneosly'''

from myutil import CountingSemaphore, UP, DOWN
from multiprocessing import Pool 

import time
import sys

pno_base = 121800

available_seats = [i for i in range(1, 10)]
n = len(available_seats)

booked_seats = []

semaphore = CountingSemaphore(n)

def print_seats(seat_state):
    '''printing seats.'''
    
    seat_state = [str(x) for x in seat_state]
    print('available seats : ', ' '.join(seat_state))

def auto_book(process, seatno):
    '''Auto book available seat for
Passenger in the wait queue.'''

    print('applying auto-booking')

    if process:
        process(seatno)
    

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
        DOWN(semaphore, self.book)
        
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
        '''To cancel ticket booked by the Passenger.
after cancel call UP and if there is waiting
book ticket for that passenger.'''
        
        cindex = booked_seats.index(self.myseat)
        canceled = booked_seats.pop(cindex)

        print('Your ticket has been canceled')

        available_seats.insert(canceled - 1, canceled)

        # changes required
        process = UP(semaphore)
        auto_book(process, canceled)
        
            
if __name__ == '__main__':
    passengers = ['hareesh',
                  'aswathy',
                  'elsa',
                  'aporva',
                  'martin',
                  'alan',
                  'rahul',
                  'anees',
                  'anoop',
                  'hari',
                  'asim',
                  'jiju',
                  'hithesh'] 

    arrangement = {} # arrange by name, object pair

    for seatno, passenger in enumerate(passengers):
        seatno += 1
        seatno %= 10

        p = Passenger(passenger)
        p.book(seatno)
        
        arrangement[passenger] = p

    p1 = arrangement['martin']
    p1.cancel()
    

