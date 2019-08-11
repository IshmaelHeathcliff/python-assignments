# coding:utf-8

def cube1(x):
	k = 0
	while k < x:
		if x - k * k * k < 1e-8:
			return k
		k += 0.001

print(cube1(10))

def cube2(x):
	a = 0
	b = x

	while b-a > 1e-8:
		if ((b + a ) / 2) ** 3 > x:
			b = (b + a ) / 2
		else:
			a = (b + a ) / 2
	
	return (b + a) / 2

print(cube2(10))
