from turtle import *
from random import randint

def direction():
    n = randint(0, 3)
    return n * 90

reset()

for i in range(100):
    fd(10)
    right(direction())

done()