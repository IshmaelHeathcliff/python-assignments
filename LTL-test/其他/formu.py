from impo import *
from BiTree import *


    form1 = form.split('(')
    for i in range(len(form1)):
        form1[i] = form1[i].split(')')
        for k in range(len(form1[i])):
            form1[i][k] = form1[i][k].split(' ')

    formu = BiTree()
    m, n = 0, 0
    for i in range(len(form1)):
        for k in range(len(form1[i])):
            if '' in form1[i][k]:
                continue
            else:
                m, n = i, k
                break
        else:
            continue
        break
    
    root = Binode(form1[m][n][-1])
    formu.set_root(root)
    for i in range(m + 1):
        for k in range(1, n):



    return form1

imp = impo()
print(formula(imp[3][1]))
