# lst是所有景点的名字表，word是用户输入

def find_by_word(lst, word):
    ans = []
    slices = []
    if len(word) > 20:
        raise ValuError("in find_by_word, we don't think it's possible for a city or a town\
         to own a name longer than 20")
    # 如果客户输入的地名在地名总集中，我们有理由相信他没有输错
    for i in range(1, len(word)):
        for j in range(0, len(word) - i + 1):
            slices.append(word[j:j + i])
    slices.append(word)
    for x in lst:
        for i in range(1, len(slices) + 1):
            if slices[-i] in x:
                if x not in ans:
                    ans.append(x)
    return ans

# name是待选名字的位置下标，re_do是待选的名字表
# 名字地点类别
def find_by_sort(lst, lst_sort, sort, word):
    if len(lst) != len(lst_sort):
        raise ValueError("in find_by_sort,\
the lenth of the two lists are not the same")
    ans = []
    for i in range(len(lst)):
        if lst_sort[i] == sort:
            ans.append(lst[i])
    return find_by_word(ans, word)

def find_by_dist(lst, lst_dist, dist, word):
    if len(lst) != len(lst_dist):
        raise ValueError("in find_by_dist,\
the lenth of the two lists are not the same")
    ans = []
    for i in range(len(lst)):
        if lst_dist[i] == dist:
            ans.append(lst[i])
    return find_by_word(ans, word)

