from SStack import *
infinity = float("inf")


class AdjGraphError(TypeError):
    pass


class GraphA:

    def __init__(self, mat=[]):
        self.mat = mat
        self.vnum = len(mat)

    def add_edge(self, vi, vj):
        if not (0 <= vi < self.vnum and 0 <= vj < self.vnum):
            raise AdjGraphError
        row = self.mat[vi]
        for i in range(len(row)):
            if row[i] == vj:
                return
        else:
            i = len(row)  # adjust for the new entry at the enddd
        self.mat[vi].insert(i, vj)

    def out_edges(self, vi):
        if not (0 <= vi < self.vnum):
            raise AdjGraphError
        return self.mat[vi]

    def get_paths(self): # 给出图内从0开始的全部只有一个圈的路径
        st = SStack()
        res = []
        links = self.mat.copy()
        st.push([0, links[0].copy()])
        path = [0]
        while not st.is_empty():
            link = st.pop()
            if link[1] == []:
                if links[link[0]] == []:
                    res.append(path.copy())
                path.pop()
                continue
            nxt = link[1].pop()
            st.push(link)
            st.push([nxt, links[nxt].copy()])
            if nxt in path:
                path.append(nxt)
                res.append(path.copy())
                path.pop()
                st.pop()
                continue

            path.append(nxt)

        return res

    def __str__(self):
        return str(self.mat)
