##张浩然
##1500010684
##40min
##Computing 1.4

print('please input binary numbers;input \'end\' to exit')

while True:
    a=input('number:')

#输入end退出
    if a=='end':
        break
#检查是否是二进制数
    elif a.count('0')+a.count('1')+a.count('.')+a.count('-')!=len(a) \
         or a.count('-')>1 or a.count('.')>1:
        print('please check')

#分别检查是否有小数点或负号，将整数部分和小数部分分片
    else:
        sign=''
        if '-' in a:
            a=a[1:]
            sign='-'
        if '.' in a:
            x=a.index('.')
            c=a[x+1:]
            b=a[:x]
        else:
            b=a
            c=''
        

        len1=len(b)
        d=-1
        y=0
        z=0
            
#整数部分和小数部分每位依次转化再加起来
        for i in b:
            y=y+int(i)*2**(len1-1)
            len1=len1-1
        for j in c:
            z=z+int(j)*2**d
            d=d-1
        print(sign+str(y+z))

print('Thanks for using.')
                
        
