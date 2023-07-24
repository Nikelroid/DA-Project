class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.modified_nodes = []
        self.modified_set = set()

    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def find_save(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find_save(self.parent[x])
            if not x in self.modified_set:
                self.modified_nodes.append(x)
                self.modified_set.add(x)
        return self.parent[x]

    def union_save(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
            if not xset in self.modified_set:
                self.modified_nodes.append(xset)
                self.modified_set.add(xset)
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
            if not yset in self.modified_set:
                self.modified_nodes.append(yset)
                self.modified_set.add(yset)
        else:
            self.parent[yset] = xset
            if not yset in self.modified_set:
                self.modified_nodes.append(yset)
                self.modified_set.add(yset)
            self.rank[xset] = self.rank[xset] + 1
            if not xset in self.modified_set:
                self.modified_nodes.append(xset)
                self.modified_set.add(xset)

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

    def refine(self, rank, par):
        for i in self.modified_nodes:
            self.parent[i] = par[i]
            self.rank[i] = rank[i]
        self.modified_nodes = []
        self.modified_set = set()


def kruskal(edges, n, keys, q):
    mask = ["YES"] * q
    rank = [1] * n
    parent = [i for i in range(n)]
    dsu = DSU(n)
    for k in keys:
        numq = 0
        for query, group in edges[k].items():
            dsu.refine(rank, parent)
            if query == 0:
                for edge in group:
                    u, v = edge
                    if dsu.find_save(u - 1) != dsu.find_save(v - 1):
                        dsu.union_save(u - 1, v - 1)
            elif mask[query - 1]=="YES":
                for edge in group:
                    u, v = edge
                    if dsu.find_save(u - 1) == dsu.find_save(v - 1):
                        mask[query - 1] = "NO"
                        break
                    else:
                        dsu.union_save(u - 1, v - 1)
            numq += 1
        for i in dsu.modified_nodes:
            rank[i] = dsu.rank[i]
            parent[i] = dsu.parent[i]
        #rank, parent = [i for i in dsu.rank], [i for i in dsu.parent]
        dsu.modified_nodes = []
        dsu.modified_set = set()

    return mask


import sys

edges = {}
edges_list = []

n, m = list(map(int, sys.stdin.readline().strip().split()))
for i in range(m):
    ed = list(map(int, sys.stdin.readline().strip().split()))
    edges_list.append(ed)
    if not ed[2] in edges:
        edges[ed[2]] = {}

keys = sorted(list(edges.keys()))
q = int(sys.stdin.readline().strip())

for i in range(q):
    indexes = list(map(int, sys.stdin.readline().strip().split()))[1:]
    for j in indexes:
        sdge = edges_list[j - 1]
        if i + 1 in edges[sdge[2]]:
            edges[sdge[2]][i + 1].append((sdge[0], sdge[1]))
        else:
            edges[sdge[2]][i + 1] = [(sdge[0], sdge[1])]

for edge in edges_list:
    if 0 in edges[edge[2]]:
        edges[edge[2]][0].append((edge[0], edge[1]))
    else:
        edges[edge[2]][0] = [(edge[0], edge[1])]
print('\n'.join(sub for sub in kruskal(edges, n, keys, q)))