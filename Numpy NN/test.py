import numpy as np

class testclass:
    def __init__(self, x):
        self.x = x
    def test(self):
        self.x[0] += 1

x = [1,2,3,4]
print(x[:2])
print(x[2:])

