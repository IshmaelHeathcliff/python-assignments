# not have to be put into a special place at first
# but at first we can think that not A is () not (A) that a formula should not satisfy A

# typer is used to split the formula into a smaller size

quantities = ["X", "F", "G", "U", "R", "E", "A"]
skill = ["(", ")"]
inner = ["and", "or", "not"]

def typer(str_):
    if not isinstance(str_, str):
        raise TypeError("in typer, str_ is not a str")
    if str_[0] != "(" or str_[-1] != ")":
        raise TypeError("in typer, str_ beginner or laster is not brackets")
    new_str = str_[1:-1]
    if new_str.count("(") == 0:
        return True
    len_ = len(str_)
    j = 0
    for i in range(len_ - 2):
        if new_str[i] == "(":
            j += 1
        if new_str[i] == ")":
            j += -1
        if j == 0:
            j = i + 1
            break
    # we can check here
    if new_str[j + 1] in quantities:
        return [new_str[j + 1], new_str[0:j], new_str[j + 3:]]
    if new_str[j + 1:j + 4] in inner:
        return [new_str[j + 1:j + 4], new_str[0:j], new_str[j + 5:]]
    if new_str[j + 1:j + 3] == "or":
        return ["or", new_str[0:j], new_str[j + 4:]]
    return True
# if we return True, it means that str_ is a Atomic Proposition(Transition)

# str_1="((f1) U (f2 and f3))"
# print(typer(str_1))
# str_2="((f1) and (f2 and f3))"
# print(typer(str_2))
# str_3="((f1) or (f2 and f3))"
# print(typer(str_3))

# now we get it!!!

# f1 f2 is the type of str
# now we set the class "transition"
# in this class, a transition's satisfying is given

class transition:
    def __init__(self, name, state1 = None, state2 = None):
        if not isinstance(name, str):
            raise TypeError("in __init__ of transition, name is not str")
        self.name = name
        self.state1 = state1
        self.state2 = state2
    
    def trans_satisfy(self, f1):
        if not isinstance(f1, str):
            raise TypeError("in trans_satisfy, f1 is not a str")
        if f1[0] != "(" or f1[-1] != ")":
            raise TypeError("in trans_satisfy, f1 does not has a porper form")
        if f1[1:-1] == "True":
            return True
        return self.name == f1[1:-1]

class path:
    def __init__(self, s_num = 0):
        self.path = []
        self.s_num = 0

    def is_empty(self):
        return len(self.path) == 0

    def print_path(self):
        ans = ""
        for i in range(self.s_num - 1):
            ans += self.path[i].name + "->"
        ans += self.path[-1].name
        return ans

    def add_transition(self, transition):
        self.path.append(transition)
        self.s_num += 1

    def middle(self, i):
        ans = path(s_num = 0)
        if self.is_empty():
            raise ValueError("in middle, empty path has no sub path.")
        if i > self.s_num - 1:
            raise ValueError("in middle, we don't have enough state.")
        for j in range(i, self.s_num):
            ans.add_transition(self.path[i])
        return ans
# f1 is a one--type str
    def satisfy_f1(self, f1):
        if f1 == "True":
            return True
        return self.path[0].trans_satisfy(f1)

    def satisfy_not_f1(self, f1):
        return not self.path[0].trans_satisfy(f1)

    def satisfy_f1_and_f2(self, f1, f2):
        return self.satisfy_all(f1) and self.satisfy_all(f2)

    def satisfy_f1_or_f2(self, f1, f2):
        return self.satisfy_all(f1) or self.satisfy_all(f2)

    # X is a little complex, for it can Underflow, then we regard it as False@.@
    def satisfy_X_f1(self, f1):
        if self.s_num <= 1:
            return False
        return self.middle(1).satisfy_all(f1)

    def satisfy_F_f1(self, f1):
        for i in range(self.s_num):
            if self.middle(i).satisfy_all(f1):
                return True
        return False

    def satisfy_G_f1(self, f1):
        for i in range(self.s_num):
            if not self.middle(i).satisfy_all(f1):
                return False
        return True

    def satisfy_U_f1_f2(self, f1, f2):
        cut = -1
        for i in range(self.s_num):
            if self.middle(i).satisfy_all(f2):
                cut = i
                break
        if cut == 0:
            return True
        if cut == -1:
            return False
        for i in range(i):
            if not self.middle(i).satisfy_all(f1):
                return False
        return True

    def satisfy_R_f1_f2(self, f1, f2):
        cut = -1
        for i in range(self.s_num):
            if self.middle(i).satisfy_all(f1):
                cut = i
                break
        if cut == -1:
            cut = self.s_num - 1
        for i in range(0, cut + 1):
            if not self.middle(i).satisfy_all(f2):
                return False
        return True

# f has a long form
    def satisfy_all(self, f):
        if typer(f) == True:
            return self.satisfy_f1(f)
        info = typer(f)
        if info[0] == "and":
            return self.satisfy_f1_and_f2(info[1], info[2])
        if info[0] == "not":
            return not self.satisfy_all(info[2])
        if info[0] == "or":
            return self.satisfy_f1_or_f2(info[1], info[2])
        if info[0] == "X":
            return self.satisfy_X_f1(info[2])
        if info[0] == "F":
            return self.satisfy_F_f1(info[2])
        if info[0] == "G":
            return self.satisfy_G_f1(info[2])
        if info[0] == "U":
            return self.satisfy_U_f1_f2(info[1], info[2])
        if info[0] == "R":
            return self.satisfy_R_f1_f2(info[1], info[2])
