from math import *

def multiple(n):#阶乘
    return n if n == 1 else n * multiple(n-1)

def sinx(x):
    n = 0
    s1 = 0
    s2 = 0
    x = x % (2 * pi)
    while True:
        s2 += x ** (2 * n + 1) / multiple(2 * n + 1) * (-1) ** n
        if abs(s1 - s2) < 1e-16:
            return s2
        else:
            n += 1
            s1 = s2
            
