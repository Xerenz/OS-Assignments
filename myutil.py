from collections import deque

class Semaphore:

    def __init__(self):
        self.value = 0
        self.queue = deque([])

    def P(self):
        self.value -= 1

    def V(self):
        self.value += 1
