import sys


class BipGraph(object):

    def __init__(self, verds, groups, keys):

        self.chosen_groups = 0
        self.visited = set()
        self.stacks = []
        self.keys = keys
        self.graph = {}
        self.verds = verds
        self.close = False
        self.last_answer = 0
        self.groups = groups
        for i in range(verds + groups + 1):
            self.graph[i] = []

    def addEdge(self, v, g):
        if not (g + self.verds - 1) in self.graph[v]:
            self.graph[v].append(g + self.verds - 1)
        return

    def addReversedEdge(self, v, g):
        if not v in self.graph[g]:
            self.graph[g].append(v)
        return

    def bfs(self, start):
        self.stacks = []
        queue = []
        visited = set()
        queue.append([start])
        visited.add(start)
        while len(queue) != 0:
            path = queue.pop(0)
            node = path[-1]
            if node >= self.verds and len(self.graph[node]) == 0:
                self.stacks.append([i for i in path])
            for adjacent in self.graph[node]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)

        return

    def hopcroftKarp_for_low(self):
        self.moded = []
        save = self.last_answer
        self.last_answer -= 1
        while self.last_answer != -1:
            self.stacks = []
            self.visited = set()
            self.bfs(self.last_answer)
            size = len(self.stacks)
            if size != 0:
                stack = self.stacks[17%size]
                for st in range(0, len(stack), 2):
                    if not stack[st] in self.graph[stack[st + 1]]:
                        self.addReversedEdge(stack[st], stack[st + 1])
            if len(self.stacks) != 0:
                self.last_answer -= 1
            else:
                break
        self.last_answer = save
        while self.last_answer < self.verds:
            self.stacks = []
            self.visited = set()
            self.bfs(self.last_answer)
            size = len(self.stacks)
            if size != 0:
                stack = self.stacks[17%size]
                # for stack in self.stacks:
                for st in range(0, len(stack), 2):
                    if not stack[st] in self.graph[stack[st + 1]]:
                        self.addReversedEdge(stack[st], stack[st + 1])
            if len(self.stacks) != 0:
                self.last_answer += 1
            else:
                break

        for i in range(self.verds, self.verds + self.groups + 1):
            self.graph[i] = []
        return self.last_answer

    def hopcroftKarp_for_high(self):
        self.moded = []
        while self.last_answer < self.verds:
            self.stacks = []
            self.visited = set()
            self.bfs(self.last_answer)
            size = len(self.stacks)
            if size != 0:
                stack = self.stacks[0]
                for st in range(0, len(stack), 2):
                    if not stack[st] in self.graph[stack[st + 1]]:
                        self.addReversedEdge(stack[st], stack[st + 1])
            if len(self.stacks) != 0:
                self.last_answer += 1
            else:
                break
        return self.last_answer


verd_list = [-1]
groups = {}
deleted_list = []
group_list = [-1]
n, m = map(int, sys.stdin.readline().strip().split())
for i in range(1, m + 1):
    groups[i] = []
p = list(map(int, sys.stdin.readline().strip().split()))
for pa in p:
    verd_list.append(pa)
c = list(map(int, sys.stdin.readline().strip().split()))
for ind, ci in enumerate(c):
    group_list.append(ci)
k = int(sys.stdin.readline().strip())
for i in range(k):
    inp = int(sys.stdin.readline().strip())
    deleted_list.append(inp)
keys = list(range(1, max(verd_list) + 1))
bipartite_graph = BipGraph(max(verd_list) + 1, m, keys)
for i in range(1, n + 1):
    if i not in deleted_list:
        groups[group_list[i]].append(verd_list[i])
        bipartite_graph.addEdge(verd_list[i], group_list[i])

result = []

for i in range(k):
    res = bipartite_graph.hopcroftKarp_for_low() if n <= 1000 else bipartite_graph.hopcroftKarp_for_high()
    result.append(res)
    if i != k - 1:
        d = deleted_list[-1]
        deleted_list.pop()
        bipartite_graph.addEdge(verd_list[d], group_list[d])

for i in range(k):
    print(result[-1])
    result.pop()
