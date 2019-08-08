#-*-coding:utf-8-*-
from Graph import *
from class_in_all import *


def ContentDict(): # 得出名称下标表
    dic = {}
    contents = open('content.dat', 'r', encoding='utf-8').readlines()
    for i in range(len(contents)):
        name = contents[i].split(' ')[0]
        dic.update({name: i})
    return dic

contentdict = ContentDict()


def ContentList(): # 得出全部名称表、地区表、类型表
    content = open("content.dat", "r", encoding="utf-8").readlines()
    name, dist, sor = [], [], []
    for i in range(len(content)):
        cont = content[i].strip('\n').split(sep=' ')
        name.append(cont[0])
        dist.append(cont[1])
        sor.append(cont[2])
    return name, dist, sor

clist = ContentList()


def gen_land_list(): # 生成所需的land_list
    land_list = []
    name, dist, sor = clist[0], clist[1], clist[2]
    for i in range(len(name)):
        land = landscape(name[i], dist[i], sor[i])
        land_list.append(land)
    return land_list

land_list = gen_land_list()


def Edges(ls): # 直接生成子图，不使用
    lst = ls[:]
    count, cou = 0, 0
    vnum = len(lst)
    graph_money, graph_time, graph_line = GraphAL(), GraphAL(), GraphAL()
    for i in range(vnum):
        graph_time.add_vertex()
        graph_money.add_vertex()
        graph_line.add_vertex()

    file = open("links.dat", "r", encoding="utf-8")
    while True:
        link = file.readline().strip('\n')
        if link == '' or cou == len(lst):
            break
        if count == lst[cou]:
            lin = link.split(sep=' ')
            for i in range(len(lin)):
                li = lin[i].split(sep=',')
                if int(li[0]) in lst:
                    ind = lst.index(int(li[0]))
                    graph_time.add_edge(cou, ind, int(li[1]))
                    graph_money.add_edge(cou, ind, int(li[2]))
                    graph_line.add_edge(cou, ind, int(li[3]))
            cou += 1
        count += 1
    return graph_money, graph_time, graph_line


def AEdges(): # 由文档生成总图
    links = open("links.dat", "r", encoding="utf-8").readlines()
    lst = [[] for i in range(len(links))]
    all_graph_time = GraphAL(lst)
    all_graph_money = GraphAL(lst)
    all_graph_line = GraphAL(lst)

    for i in range(len(links)):
        link = links[i].strip('\n').split(sep=' ')
        if link == ['']:
            continue
        for k in range(len(link)):
            lin = link[k].split(sep=',')
            ind = int(lin[0])
            all_graph_time.add_edge(i, ind, int(lin[1]))
            all_graph_money.add_edge(i, ind, int(lin[2]))
            all_graph_line.add_edge(i, ind, int(lin[3]))

    return web(len(clist[0]), land_list, all_graph_money, all_graph_time, all_graph_line)
