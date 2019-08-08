from Graph import *
from PrioQueue import *
from GShortestPath import *
from GSpanTree import *
from User import *
infinity = float("inf")


# 这是根据关键字找地点的方法，已经形成了某个依据属性的表后，通过关键词匹配来解决问题
# 最终输出一个yield出的迭代器，将其list化后就可以向末端输出了
def find_by_word(lst, word):
    # 这个是字符串匹配函数,word是客户输入，lst是循环的东西
    # 最好排成优先队列
    # 若没找到，我们可以造一个关于word的任意位置的切片，长度比word短，由此来寻找想要的名称
    # 由于景点，地名的长度一般不长，所以即使这里的时间代价极高，我们也可以保证这样做不会引发混乱
    ans = []
    for x in lst:
        if word == x:
            ans.append(x)
    if len(word) > 20:
        raise ValuError("in find_by_word, we don't think it's possible for a city or a town\
         to own a name longer than 20")
    # 如果客户输入的地名在地名总集中，我们有理由相信他没有输错
    if ans != []:
        return ans
    slices = []
    for i in range(len(word)):
        # 这里为了保证效率，我们可以通过控制内部循环来使得表中名字串长度从小到大排列
        # 并且这样排出来的结果是相似度高的在前面
        for j in range(0, len(word) - i + 1):
            slices.append(word[j:j + i])
    for x in lst:
        for i in range(1, len(word)):
            if slices[-i] in x:
                ans.append(x)
    return ans


categorys = {"历史文化", "现代都市", "山区", "海景", "综合"}
infnum = float("inf")


class web:
    # land_list是一个list对象，适用相应方法

    def __init__(self, lnum=0, land_list=[], graph_money=GraphAL(), graph_time=GraphAL(), graph_line=GraphAL()):
        self.graph_money = graph_money
        self.graph_time = graph_time
        self.graph_line = graph_line
        self.lnum = lnum
        self.land_list = land_list

    def is_empty(self):
        return self.lnum == 0
    # 获得所有景点名称，用list储存
    # self._land_list是以landscape为元素的表

    def _get_name(self):
        if self.is_empty():
            raise WebLandsError("in 'get_all_position'")
        namee = []
        for x in self.land_list():
            namee.append(x.name)
        return namee
    # 获得所有景点位置

    def lst_pos(self, land):
        return self.land_list.index(land)

    def _get_position(self):
        if self.is_empty():
            raise WebLandsError("in 'get_all_position'")
        positionn = []
        for x in self.land_list():
            positionn.append(x.position)
        return positionn

    def add_land(self, landscape):
        self.land_list.append(landscape)
        self.graph_money.add_vertex()
        self.graph_time.add_vertex()
        self.graph_line.add_vertex()
        self.lnum += 1

    # 如果不设置money，time或line，自然landscape之间没有边相连

    def set_all(self, land1, land2, money=infnum, time=infnum, line=1):
        graph_money.add_edge(self.land_list().index(land1),
                             self.land_list().index(land2), money)
        graph_time.add_edge(self.land_list().index(land1),
                            self.land_list().index(land2), time)
        graph_line.add_edge(self.land_list().index(land1),
                            self.land_list().index(land2), line)

# 以下基于Dijkstra算法来搞定最短路径问题，可同时作用于时间，金钱和路径长度做邻接图
    def set_money(self, land1, land2, money):
        self.graph_money.add_edge(self.land_list.index(land1),
                                  self.land_list.index(land2), money)

    def get_money(self, land1, land2):
        a = self.graph_money.get_edge(self.land_list.index(land1),
                                      self.land_list.index(land2))
        return a

    def set_time(self, land1, land2, time):
        self.graph_money.add_edge(self.land_list.index(land1),
                                  self.land_list.index(land2), time)

    def get_time(self, land1, land2):
        a = self.graph_time.get_edge(self.land_list.index(land1),
                                     self.land_list.index(land2))
        return a

    def set_line(self, land1, land2, line):
        self.graph_line.add_edge(self.land_list.index(land1),
                                 self.land_list.index(land2), line)

    def get_line(self, land1, land2):
        a = self.graph_line.get_edge(self.land_list.index(land1),
                                     self.land_list.index(land2))
        return a

# shortestmoney等开始


def shortest_money(web, land1, land2):
    vi = web.lst_pos(land1)
    vj = web.lst_pos(land2)
    if vi == vj:
        raise ValuError("in shortest_money,\
         if the begining is the same as the ending, you don't have to pay anything")
    path = dijkstra_shortest_paths(web.graph_money, vi)
    path_list = [vi]
    while vi != path[vj][0]:
        path_list.append(path[vj][0])
        vi = path[vj][0]
    return path_list, path[vj][1]


def shortest_money_str(web, land1, land2):
    str_ = ""
    path, pay = shortest_money(web, land1, land2)
    for i in range(len(path)):
        str_ += str(web.land_list[path[i]].name)
        str_ += "->"
    str_ += land2.name
    return "所求的最短路money路径为", str_, "总money代价为", pay


def shortest_time(web, land1, land2):
    vi = web.lst_pos(land1)
    vj = web.lst_pos(land2)
    if vi == vj:
        raise ValuError("in shortest_time,\
         if the begining is the same as the ending, you don't have to pay anything")
    path = dijkstra_shortest_paths(web.graph_time(), vi)
    path_list = [vi]
    while vi != vj:
        path_list.append(path[vj][0])
        vi = path[vj][0]
    return path_list, path[vj][1]


def shortest_time_str(web, land1, land2):
    str_ = ""
    path, pay = shortest_time(web, land1, land2)
    for i in range(len(path)):
        str_ += str(path[i])
    return "所求的最短路time路径为", str_, "总time代价为", pay


def shortest_line(web, land1, land2):
    vi = web.lst_pos(land1)
    vj = web.lst_pos(land2)
    if vi == vj:
        raise ValuError("in shortest_line,\
         if the begining is the same as the ending, you don't have to pay anything")
    path = dijkstra_shortest_paths(web.graph_line(), vi)
    path_list = [vi]
    while vi != vj:
        path_list.append(path[vj][0])
        vi = path[vj][0]
    return path_list, path[vj][1]


def shortest_time_str(web, land1, land2):
    str_ = ""
    path, pay = shortest_line(web, land1, land2)
    for i in range(len(path)):
        str_ += str(path[i])
    return "所求的最短路line路径为", str_, "总line代价为", pay
# shortest等结束


class landscape:  # landscape代表一个景点，rank表示在图中list的位置

    def __init__(self, name, position, category=None, hot=0):  # 其中position是一个数，代表一个景点
        self.name = name
        self.position = position
        self.category = category
        self.hot = hot

    def position(self):
        return self._position

    def category(self):
        return self._category

    def name(self):
        return self._name

    def hot(self):
        return hot

    def set_category(self, sorts):
        if sorts not in categorys:
            raise ValuError("in set_category, we do not have {}".format(sorts))
        self.category = sorts

# 对于多目标问题，先用既有方法构造一个web，web保存了所有目标landscape
# 现在基于Prim算法给出一个关于多目标问题的算法，其实就是最小生成树问题


def muti_aim_solve(land_list):
    sub_web = web()
    for x in land_list:
        sub_web.add_land(x)
    lanst = web.land_list().copy()
    for x in lanst:
        for y in lanst:
            if x == y:
                continue
            vi = lst_pos(web, x)
            vj = lst_pos(web, y)

a, b, c = Edges([0, 2, 4])
lst = ["东方明珠", "西湖", "迪士尼"]
china = web(3, lst, a, b, c)
