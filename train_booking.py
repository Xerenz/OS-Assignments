from myutil import Semaphore
from myutil import P, V
from multiprocessing import Pool 

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

        self.myseat = None

    def book(self, seatno):
        if len(available_seats) == 0:
            print('No seats available.\nPushing into wait queue')
            semaphore.queue.append(self)
            
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
        
            
if __name__ == '__main__':
    p1 = Passenger('martin')
    p2 = Passenger('aswathy')

    p1.book(3)
    p2.book(3)

    p1.cancel()

    print(available_seats)
