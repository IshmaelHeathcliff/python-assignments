
i = 1
s = 0
while True:
    x = input('x' + str(i) + ':')
    if x == 'None':
        print(s / (i - 1))
        break
    else:
        s += int(x)
        i += 1
        
