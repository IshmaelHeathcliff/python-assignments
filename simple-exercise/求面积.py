#

x,y,z=float(input('a:')),float(input('b:')),float(input('c:'))

w=(x+y+z)/2

from cmath import sqrt

print('area=',sqrt(w*(w-x)*(w-y)*(w-z)))
