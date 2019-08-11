def impo():
    file = open('file.dat', 'r', encoding="utf-8")
    stat_list = file.readline().strip('\n').split()
    start = file.readline().strip('\n')

    # 修饰状态的表，将起点放在第一位
    stat_list.remove(start)
    stat_list.insert(0, start)

    trans_list = []
    trans = file.readline()
    while trans != '\n':
        trans_list.append(tuple(trans.strip('\n').split(sep=' ')))
        trans = file.readline()

    formula_list = []
    formula = file.readline()
    trans_name_list = [trans_list[i][0] for i in range(len(trans_list))] + ['True']
    while formula != '':
        formula1 = formula.strip('\n').split('(')
        for i in range(len(formula1)):
            formula1[i] = formula1[i].split(')')
            for k in range(len(formula1[i])):
                formula1[i][k] = formula1[i][k].split(' ')
                for j in range(len(formula1[i][k])):
                    if formula1[i][k][j] in trans_name_list:
                        formula1[i][k][j] = '(' + formula1[i][k][j] + ')'
                formula1[i][k] = ' '.join(formula1[i][k])
            formula1[i] = ')'.join(formula1[i])
        formula1 = '('.join(formula1)

        formula_list.append(formula1)
        formula = file.readline()

    return stat_list, trans_list, formula_list

print(impo()[2])
