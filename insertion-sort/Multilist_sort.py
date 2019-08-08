# 结果分析：以分组100为例
# 多表插入排序和表插入排序在排序过程中， 移动次数上差一个固定量，与分组组数有关，
# 多表插入排序的比较次数为表插入比较次数的1/100,
# 实际时间代价大于1/100，多表插入排序时建立附加表花费O(n)的时间代价，
# 若分组数为O(n)，则排序的时间代价变为为O(n)，建立子表的时间代价变为O(n^2)
from random import *
import time


def gen_randint(n):  # 生成数列
    lis = []
    for i in range(n):
        lis.append(randint(0, 10 * n - 1))

    return lis


class LNode:

    def __init__(self, elem, nxt=None):
        self.elem = elem
        self.nxt = nxt


class LList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def prepend(self, elem):
        self.head = LNode(elem, self.head)


def list_sort(lis):
    comp_count = 0
    mv_count = 0

    # 建立附加链表
    llist = LList()
    num = len(lis)
    res = []
    for i in range(num):
        llist.prepend(lis[-i - 1])

    pre = llist.head
    now = pre.nxt
    for i in range(1, num):
        comp = llist.head
        for k in range(i - 1):
            comp_count += 2
            if now.elem <= comp.elem:
                now = now.nxt
                llist.head = pre.nxt
                pre.nxt = now
                llist.head.nxt = comp
                mv_count += 1
                break
            if comp.elem < now.elem <= comp.nxt.elem:
                now = now.nxt
                pre.nxt.nxt = comp.nxt
                comp.nxt = pre.nxt
                pre.nxt = now
                mv_count += 1
                break
            else:
                comp = comp.nxt
        else:
            now = now.nxt
            pre = pre.nxt

    # 链表恢复成表
    nod = llist.head
    while nod.nxt != None:
        res.append(nod.elem)
        nod = nod.nxt

    return res, comp_count, mv_count


def multilist_sort(lis):
    comp_count = 0
    mv_count = 0

    num = len(lis)
    group = []
    res = []
    for i in range(100):  # 分为100组
        group.append([])

    for i in range(num):
        group[lis[i] * 10 // num].append(lis[i])

    for i in range(100):
        if group[i] != []:
            resp = list_sort(group[i])
            res += resp[0]
            comp_count += resp[1]
            mv_count += resp[2]

    return res, comp_count, mv_count

for n in [1000, 2000, 5000]:
    lis = gen_randint(n)
    time1 = time.time()
    a = multilist_sort(lis)
    time2 = time.time()
    b = list_sort(lis)
    time3 = time.time()

    print("长度为:", n)
    print("多表插入排序比较次数和移动次数:", a[1], a[2])
    print("表插入排序比较次数和移动次数:", b[1], b[2])
    print("多表插入排序所用时间:", time2 - time1, "\n表插入排序所用时间:", time3 - time2, "\n")
