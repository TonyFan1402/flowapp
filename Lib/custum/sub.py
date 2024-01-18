import numpy

class sub:
    def __init__(self):
        #input
        self.x = None
        self.y = None
        #output
        self.sum = None

    def take_sum(self):
        self.sum = self.x - self.y

    def process(self):
        self.take_sum()