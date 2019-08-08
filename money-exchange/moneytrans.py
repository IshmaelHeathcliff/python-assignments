# 初始币种及最终币种放在表和图的第一位，表和图位置对应
# 实例数据为网上所查， 两个币种相互之间的汇率不为倒数，但还是把这种情况剔除了
from Graph import Graph


def money_gain(lst, graph):
    result = []

    assert(len(lst) == graph.vertex_num())
    for i in range(1, len(lst)):
        for k in range(1, len(lst)):
            if i == k:
                continue
            edge1 = graph.get_edge(0, i)
            edge2 = graph.get_edge(i, k)
            edge3 = graph.get_edge(k, 0)
            rate = edge1 * edge2 * edge3
            if rate > 1:
                result.append(['{}——>{}——>{}——>{}, 倍率为'.format(
                    lst[0], lst[i], lst[k], lst[0]), rate])
    # 用倍率排序
    def comp(x):
        return x[1]
    result.sort(key=comp, reverse=True)

    for i in range(len(result)):
        result[i][1] = str(result[i][1])
        result[i] = ''.join(result[i])
    return '\n'.join(result)

lst = ['人民币CNY', '美元USD', '日元JPY', '欧元EUR',
       '英镑GBP', '韩元KRW', '港元HKD', '澳元AUD', '加元CAD']

gra = Graph([[1, 0.1454, 16.5651, 0.1354, 0.1149, 168.7645, 1.1279, 0.1947, 0.1921],
             [6.8771, 1, 114.03, 0.9321, 0.7905, 1161.59, 7.7564, 1.3403, 1.323],
             [0.06037, 0.008770, 1, 0.008175, 0.006932, 10.1867, 0.06802, 0.01175, 0.01160],
             [7.3998, 1.076, 122.3314, 1, 0.8480, 1246.1538, 8.3211, 1.4379, 1.4193],
             [8.7002, 1.2658, 144.2594, 1.1793, 1, 1469.5275, 9.8126, 1.6956, 1.6737],
             [0.005925, 0.0008609, 0.09817, 0.0008025, 0.0006805, 1, 0.006677, 0.001154, 0.001139],
             [0.8866, 0.1289, 14.7014, 0.1205, 0.1019, 149.8865, 1, 0.1729, 0.1705],
             [5.1283, 0.7461, 85.0173, 0.6967, 0.5896, 866.9135, 5.7838, 1, 0.9863],
             [5.1993, 0.7560, 86.1949, 0.7063, 0.5978, 878.9219, 5.8639, 1.0139, 1]])

print(money_gain(lst, gra))
