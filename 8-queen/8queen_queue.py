from SQueue import *


def QueenQueue(row):
    res_sq = SQueue()
    for i in range(row):
        res_sq.enqueue([i + 1])

    while not res_sq.is_empty():
        res = res_sq.dequeue()

        for test in set(range(1, row + 1)) - set(res):  # 待测坐标不包含已经有的坐标
            for i in range(len(res)):  # 对坐标是否符合的检验
                if test == res[i] + i + 1 or test == res[i] - i - 1:
                    break
            else:
                res_sq.enqueue([test] + res)  # 符合的结果入列

        while len(res_sq.first()) == row:
            res = res_sq.dequeue()
            print(res)
            if res_sq.is_empty():
                break

QueenQueue(8)
