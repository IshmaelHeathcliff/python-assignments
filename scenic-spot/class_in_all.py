from Graph import *
class web:
#land_list是一个list对象，适用相应方法
    def __init__(self, lnum = 0, land_list = [], graph_money = GraphAL()\
                 , graph_time = GraphAL(), graph_line = GraphAL()):
        self.graph_money = graph_money
        self.graph_time = graph_time
        self.graph_line = graph_line
        self.lnum = lnum
        self.land_list = land_list.copy()

    def is_empty(self):
        return self.lnum == 0
    # 获得所有景点名称，用list储存
    # self._land_list是以landscape为元素的表

    def get_name(self):
        if self.is_empty():
            raise WebLandsError("in 'get_all_name'")
        namee = []
        for x in self.land_list:
            namee.append(x.name)
        return namee
    # 获得所有景点位置
    
    def lst_pos(self, land):
        return self.land_list.index(land)

    def _get_position(self):
        if self.is_empty():
            raise TypeError("in 'get_all_position'")
        positionn = []
        for x in self.land_list():
            positionn.append(x.position)
        return positionn

    def add_land(self, land):
        self.land_list.append(land)
        self.graph_money.add_vertex()
        self.graph_time.add_vertex()
        self.graph_line.add_vertex()
        self.lnum += 1

##    def remove_land(self, land):
##        lst_pos = self.lst_pos
##        self.land_list.pop(lst_pos)
##        for

    #如果不设置money，time或line，自然landscape之间没有边相连

    def set_all(self, land1, land2, money = infinity, time = infinity, line = infinity):
        graph_money.add_edge(self.lst_pos(land1),\
         self.lst_pos(land2), money)
        graph_time.add_edge(self.lst_pos(land1),\
         self.lst_pos(land2), time)
        graph_line.add_edge(self.lst_pos(land1),\
         self.lst_pos(land2), line)
    
# 以下基于Dijkstra算法来搞定最短路径问题，可同时作用于时间，金钱和路径长度做邻接图
    def set_money(self, land1, land2, money):
        self.graph_money.add_edge(self.lst_pos(land1),\
            self.lst_pos(land2), money)

    def get_money(self, land1, land2):
        a = self.graph_money.get_edge(self.lst_pos(land1),\
                                      self.lst_pos(land2))
        return a
    
    def set_time(self, land1, land2, time):
        self.graph_time.add_edge(self.lst_pos(land1),\
         self.lst_pos(land2), time)

    def get_time(self, land1, land2):
        a = self.graph_time.get_edge(self.lst_pos(land1),\
                                      self.lst_pos(land2))
        return a

    def set_line(self, land1, land2, line):
        self.graph_line.add_edge(self.lst_pos(land1),\
         self.lst_pos(land2), line)

    def get_line(self, land1, land2):
        a = self.graph_line.get_edge(self.lst_pos(land1),\
                                      self.lst_pos(land2))
        return a

class landscape:  # landscape代表一个景点，rank表示在图中list的位置

    def __init__(self, name, position, category = None):  # 其中position是一个数，代表一个景点
        self.name = name
        self.position = position
        self.category = category

    def position(self):
        return self._position

    def category(self):
        return self._category

    def name(self):
        return self._name

    def set_category(self, sorts):
        if sorts not in categorys:
            raise ValuError("in set_category, we do not have {}".format(sorts))
        self.category = sorts
