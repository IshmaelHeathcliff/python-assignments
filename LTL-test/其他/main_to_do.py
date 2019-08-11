from Kripke import*
from path_trans import*

# the following is experiment

##tran1 = transition("t1")
##tran2 = transition("t2")
##tran3 = transition("t3")
##tran4 = transition("t4")
##path1 = path()
##path1.add_transition(tran1)
##path1.add_transition(tran2)
##path1.add_transition(tran3)
##path1.add_transition(tran2)
##print(path1.satisfy_all("((True) R (t3))"))
##print(path1.satisfy_all("(() not ((True) R (t3)))"))
##print(path1.satisfy_all("((t3) U (t2))"))
##print(path1.satisfy_all("((True) U (t1))"))

def enum_path(lst):
    ans = []
    for i in range(len(lst)):
        x = path(s_num = 0)
        for j in range(len(lst[i])):
            x.add_transition(transition(lst[i][j]))
        ans.append(x)
    return ans

def LTL_check(lst, formula):
    ans = enum_path(lst)
    len_ans = len(ans)
    for i in range(len_ans):
        if not ans[i].satisfy_all(formula):
            counter_example = ans[i].print_path()
            return "False," + "the counter example could be:" + str(counter_example)
    return True

lst = [['off', 'solve', 'coffee'], ['off', 'solve', 'break'],
 ['off', 'repair'], ['coin', 'coffee'],
 ['coin', 'break', 'solve'], ['coin', 'break', 'repair']]
formu_0 = "(True U ((coin) and (() X (() not (coffee)))))"
formu_1 = "(() not (True U ((coin) and (() X (() not (coffee))))))"
formu_2 = "(() not (True U ((() not (coin)) and (() X (() not (coffee))))))"

print(LTL_check(lst, formu_0))
print(LTL_check(lst, formu_1))
print(LTL_check(lst, formu_2))

# out put is as follows:
##False,the counter example could be:off->solve->coffee
##True
##True





