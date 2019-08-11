from Graph import *
from PrioQueue import *
from GShortestPath import *
from GSpanTree import *
from search_by_sth import *
from class_in_all import *


infinity = float("inf")

categorys = {"历史文化", "现代都市", "山区", "海景", "综合"}

def transname(sorting):
    if sorting == "money":
        return "金钱"
    elif sorting == "time":
        return "时间"
    elif sorting == "line":
        return "换乘次数"
    else:
        raise ValueError("in transname, 'sorting' is not found")

#shortestmoney等开始
#shortest给出的是 中途点的位置，代价总和的二元组
#总共六个函数
#shortest_many
#shortest_many_str
#shortest_many_str_mathe
#muti_many_solve_ans
#muti_many_solve_str
#muti_many_solve_str_mathe
def load_graph(web, sorting):
    if sorting == "money":
        return web.graph_money
    elif sorting == "time":
        return web.graph_time
    elif sorting == "line":
        return web.graph_line
    else:
        raise ValueError("in load_graph, 'sorting' is not found")

def shortest_many(web, land1, land2, sorting):
    graph_To = GraphAL()
    graph_To = load_graph(web, sorting)
    vi = web.lst_pos(land1)
    vj = web.lst_pos(land2)
    if vi == vj:
        raise ValueError("in shortest_many,ifthe begining is the same as the ending, you don't have to pay anything")
    path = dijkstra_shortest_paths(graph_To, vi)
    if path[vj] == None:
        return None
    path_list = [vi]
    while vi != path[vj][0]:
        path_list.append(path[vj][0])
        vi = path[vj][0]
    return path_list, path[vj][1]

def shortest_many_str(web, land1, land2, sorting):
    str_ = ""
    path, pay = shortest_many(web, land1, land2, sorting)
    for i in range(len(path)):
        str_ += str(web.land_list[path[i]].name)
        str_ += "->"
    str_ += land2.name
    return str_ + " 总{}:".format(transname(sorting)) + str(pay)

def shortest_many_str_mathe(web, vi, vj, sorting):
    land1 = web.land_list[vi]
    land2 = web.land_list[vj]
    return shortest_many_str(web, land1, land2, sorting)

def shortest_many_str_mathe_three(web, vi, vj):
    sorting = ["money","time","line"]
    return shortest_many_str_mathe(web, vi, vj, sorting[0]),\
           shortest_many_str_mathe(web, vi, vj, sorting[1]),\
           shortest_many_str_mathe(web, vi, vj, sorting[2])

# muti_many_solve_ans(网络， 景点表， 起始景点， 查找类别)
def muti_many_solve_ans(web, land_list, start, sorting):
    graph_To = load_graph(web, sorting)
    sub_web = muti_aim_solve_web(web, land_list)
    if start not in sub_web.land_list:
        raise ValueError("in muti_aim_solve_ans, we do not involve start")
    lnum = sub_web.lnum
    start_pos = sub_web.lst_pos(start)
    orders = cnn(lnum - 2)
    #[0到（目标点个数-1）的排列]=[1到目标点个数的排列]
    leno = len(orders)
    for i in range(leno):
        for j in range(lnum - 1):
            if orders[i][j] >= start_pos:
                orders[i][j] += 1

    spend = infinity
    save_way = []

    for i in range(leno):
        plen = 0
        for j in range(lnum - 1):
            if j == 0:
                if shortest_many(web, start,\
                                      sub_web.land_list[orders[i][j]], sorting) == None:
                    continue
                plen = shortest_many(web, start,\
                                      sub_web.land_list[orders[i][j]], sorting)[1]
            else:
                if shortest_many(web,\
                                       sub_web.land_list[orders[i][j - 1]],\
                                       sub_web.land_list[orders[i][j]], sorting) == None:
                    continue
                plen += shortest_many(web,\
                                       sub_web.land_list[orders[i][j - 1]],\
                                       sub_web.land_list[orders[i][j]], sorting)[1]
        if plen < spend:
            spend = plen
            save_way = orders[i]
    return spend, save_way, sub_web

#输出：代价，子图中路径【0，2，4，1】代表从3出发，3-0-2-4-1，子图

def muti_many_solve_str(web, land_list, start, sorting):
    spend, way, sub_web = muti_many_solve_ans(web, land_list, start, sorting)
    str_ = start.name
    for i in range(len(way)):
        str_ = str_ + "->" + sub_web.land_list[i + 1].name
    return str_ + " 总{}为:".format(transname(sorting)) + str(spend)

def muti_many_solve_str_mathe(web, lst, vi, sorting):
    land_list = []
    for x in lst:
        land_list.append(web.land_list[x])
    start = web.land_list[vi]
    return muti_many_solve_str(web, land_list, start, sorting)

def muti_many_solve_str_mathe_three(web, lst, vi):
    sorting = ["money","time","line"]
    return muti_many_solve_str_mathe(web, lst, vi, sorting[0]),\
           muti_many_solve_str_mathe(web, lst, vi, sorting[1]),\
           muti_many_solve_str_mathe(web, lst, vi, sorting[2])

# shortest等6个函数等结束

def muti_aim_solve_web(big_web, aim_list):
    sub_web = web(lnum = 0, land_list = [], graph_money = GraphAL()\
                 , graph_time = GraphAL(), graph_line = GraphAL())
    # 有一个特别坑的问题！！！！，为什么必须手动初始化？？值得研究
    for x in aim_list:
        sub_web.add_land(x)
    return sub_web

def show_info(web, number):
    land = web.land_list[number]
    return "景点名称:{}".format(land.name),"景点位置:{}".format(land.position),\
           "景点类型:{}".format(land.category)

#以下是内部的检查函数
#lst第一个位置是起始点
def _show_way(web, lst):
    ans = ""
    for i in len(lst):
        ans.append(web.land_list[i].name)
    return ans

# 由lst_of_num
def _check_by_num(web, lst_of_num):
    for i in range(len(lst_of_num)):
        yield web.land_list[i]

#start也是一个景点，只用做剩下的循环

#枚举函数
def cnn(n):
    if n == 1:
        return [[0,1],[1,0]]
    else:
        a = cnn(n - 1)
        b = []
        for x in a:
            x.append(n)#a is correct
        t = [0]*(n+1)
        for x in a:
            for lenth in range(n+1):# the distance
                t = [0]*(n+1)
                for inpos in range(n+1):
                    t[inpos] = (x[inpos] + lenth)%(n+1)
                b.append(t)
    return b
