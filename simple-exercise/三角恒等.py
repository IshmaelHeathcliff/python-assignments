
print('use specific numbers to prove sinx-siny=2cos[(x+y)/2]sin[(x-y)]')

from math import*

x=float(input('x:'))
y=float(input('y:'))

a=sin(x)-sin(y)
b=2*cos((x+y)/2)*sin((x-y)/2)

print('sinx-siny=',a)

print('2cos[(x+y)/2]sin[(x-y)]=',b)

if a-b==0:
    print('True')
elif a-b<1e-15:
    print('Almost')
else:
    print('False')
        

input('<enter>')
