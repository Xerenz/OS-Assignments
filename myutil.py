from collections import deque

class BinarySemaphore:
    '''Binary Semaphore class
having a value initialised 1
and a wait queue to store process.'''
    
    def __init__(self):
        self.value = 1
        self.queue = deque([])

        
def P(mutex, process):
    '''Down or wait operation
check value and apply successful ops
or usuccessful ops and process in wait-queue'''

    if mutex.value == 1: 
        mutex.value = 0
    else:
        mutex.queue.append(process)

def V(mutex):
    '''Up or signal operation
checks if wait-queue is empty
and then perform process or take from queue.'''

    if len(mutex.queue) == 0:
        mutex.value = 1
    else:
        return mutex.queue.popleft()
                
    
