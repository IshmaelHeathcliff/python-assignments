""" 图遍历与生成树
"""

from Graph import *

from SStack import SStack, StackUnderflow
from SQueue import SQueue, QueueUnderflow

# Generate the DFS sequence of rearchable vertices from v0


def DFS_seq(graph, v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum
    visited[v0] = 1
    DFS_seq = [v0]
    st = SStack()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i + 1, edges))
            if visited[v] == 0:  # unvisited node
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return DFS_seq

# Genarate span-forest of a graph, recursive definition


def DFS_span_tree(graph):
    vnum = graph.vertex_num()
    span_forest = [None] * (vnum)

    def dfs(graph, v):
        nonlocal span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)

    for v in range(vnum):
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
    return span_forest
