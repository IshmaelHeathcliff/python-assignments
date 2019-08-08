from math import sqrt

print('ax^2+bx+c=0')

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

d=b**2-4*a*c

if d>=0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print('x1=',x1,'x2=',x2)
else:
    print('no result')

input('<enter>')
