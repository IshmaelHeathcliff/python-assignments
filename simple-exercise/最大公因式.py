def gcd(x, y):#最大公因数
    m = x if x >= y else y
    n = x if x <= y else y
    
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

print(gcd(18, 60))

