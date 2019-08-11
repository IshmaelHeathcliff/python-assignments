from SStack import *


def QueenStack(row):
    res_st = SStack()
    res = ([], set(range(1, row + 1))) # 前一个表存放该层结果，后一个集合存放下一层可能的坐标
    res_st.push(res)

    while not res_st.is_empty():
        res = res_st.pop()
        if res[1] == set():  # 下一层无可能坐标则回溯
            continue

        for k in range(len(res[1])):
            test = res[1].pop()
            for i in range(0, len(res[0])):  # 检测坐标是否符合
                if test == res[0][i] + i + 1 or test == res[0][i] - i - 1:
                    break
            else:
                res_st.push(res)
                res = ([test] + res[0], set(range(1, row + 1)) -
                       set([test] + res[0]))
                if len(res[0]) == row:
                    print(res[0])
                else:
                    res_st.push(res)
                break

QueenStack(8)
