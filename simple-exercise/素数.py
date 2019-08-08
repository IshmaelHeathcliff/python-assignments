list1=[]
list2=[]
list3=[]

for a in range(2,10000):
    j=0
    for i in range(2,a):
        if a%i==0:
            break
        else:
            j=j+1
    if j==a-2:
        if a<=100:
            list1.append(a)
        elif a<=1000:
            list2.append(a)
        else:
            list3.append(a)
print('1~100:',len(list1),'100~1000:',len(list2),'1000~10000',len(list3))
