import sys


def dfs(visited, graph, node, height):  # function for dfs
    visited.add(node)
    for neighbour in graph[node]:
        if not neighbour in visited:
            children[node].append(neighbour)
            dfs(visited, graph, neighbour, height + 1)
    if height in height_set:
        heights[height].append(node)
    else:
        heights[height] = [(node)]
        height_set.add(height)

def update(node):
    if not node in leaves:
        if has_kaaj[node]:
            dp_b[node] = 0
            dp_a[node] = 1
            for child in children[node]:
                dp_a[node] *= (dp_a[child] + dp_b[child])
        else:
            if len(children[node]) <= 1:
                one_child = children[node][0]
                dp_a[node] = dp_a[one_child]
                dp_b[node] = dp_a[one_child] + dp_b[one_child]
            else:

                dp_a[node] = 0
                for child in children[node]:
                    product = 1
                    for ch in children[node]:
                        if child != ch:
                            product *= (dp_a[ch] + dp_b[ch])
                    dp_a[node] += (dp_a[child] * product)
                dp_b[node] = 1
                for child in children[node]:
                    dp_b[node] *= (dp_a[child] + dp_b[child])

n = int(sys.stdin.readline().strip())
graph = {}
children = {}
for i in range(n):
    graph[i] = []
    children[i] = []
connected = list(map(int, sys.stdin.readline().strip().split()))
list_kaj = list(map(int, sys.stdin.readline().strip().split()))
has_kaaj = [True if list_kaj[i] == 1 else False for i in range(n)]
graph_set = set()
for s, t in enumerate(connected):
    graph[s + 1].append(t)
    graph[t].append(s + 1)

visited = set()
heights = {}
leaves = set()
height_set = set()
dfs(visited, graph, 0, 0)
dp_a = [0 for i in range(n)]
dp_b = [0 for i in range(n)]

for ind, nodes in children.items():
    if len(nodes) == 0:
        if has_kaaj[ind]:
            dp_a[ind] = 1
        else:
            dp_b[ind] = 1
        leaves.add(ind)
keys = sorted(list(heights.keys()), reverse=True)[1:]
for k in keys:
    for node in heights[k]:
        update(node)
update(0)
print(dp_a[0] % (1000000007))
