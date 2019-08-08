from math import *

def nextTerm(x):
    x = x % (2 * pi)
    n = 1
    t = x
    s = 0
    while True:
        if abs(t) < 1e-10:
            return s
        else:
            s += t
            t *= - x ** 2 / (2 * n * (2 * n + 1))
            n += 1
        
