from collections import deque

class BinarySemaphore:
    '''Binary Semaphore class
having a value initialised 1
and a wait queue to store process.'''
    
    def __init__(self):
        self.value = 1
        self.queue = deque([])

class CountingSemaphore:
    '''counting semaphore class
having value passed in constructor
and a wait queue.'''

    def __init__(self, value):
        self.value = value
        self.queue = deque([])

# for binary
def P(mutex, process, args):
    '''Down or wait operation
check value and apply successful ops
or usuccessful ops and process in wait-queue'''

    if mutex.value == 1: 
        mutex.value = 0
    else:
        mutex.queue.append((process, args))

def V(mutex):
    '''Up or signal operation
checks if wait-queue is empty
and then perform process or take from queue.'''

    if len(mutex.queue) == 0:
        mutex.value = 1
    else:
        return mutex.queue.popleft()

# for counting
def DOWN(s, process, args):
    s.value -= 1

    if s.value < 0:
        s.queue.append((process, args))

def UP(s):
    s.value += 1

    if s.value < 0:
        return s.queue.popleft()
                
    
