
def fi(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fi(x - 1) + fi(x - 2)



for k in range(1, 11):
    print(fi(k))

def fib(x):
    f1 = 1
    f2 = 1
    for i in range(1,x):
        f1, f2 = f2, f1 + f2
        i += 1
    return f1
        
        
