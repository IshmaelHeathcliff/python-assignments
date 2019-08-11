from Kripke import*
from path_trans import*

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





