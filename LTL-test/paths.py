from Graph import *
from SStack import *


def paths(stat_list, trans_list): # 输入impo中的对应表，输出元素为迁移名称的路径表的表，如[["coin", "coffee"]]
    # 建立状态的图
    stat_dic = {stat_list[i]: i for i in range(len(stat_list))}
    trans_dic = {(stat_dic.get(trans_list[i][1]),
                  stat_dic.get(trans_list[i][2])): trans_list[i][0]
                 for i in range(len(trans_list))}
    trans_lis = list(trans_dic.keys())
    stat_graph = GraphA([[] for i in range(len(stat_list))])
    for x, y in trans_lis:
        stat_graph.add_edge(x, y)

    # 得到状态的路径
    paths = stat_graph.get_paths()

    # 将状态的路径转化为迁移的路径
    for i in range(len(paths)):
        num_path = paths[i]
        name_path = []
        for k in range(len(num_path) - 1):
            name_path.append(trans_dic.get((num_path[k], num_path[k + 1])))
        paths[i] = name_path

    return paths
