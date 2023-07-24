import heapq as hq
def dijkstra(graph, start):
    distances = {}
    heap = [(0, start)]

    while heap:
        dist, node = hq.heappop(heap)
        if node in distances:
            continue 
        distances[node] = dist
        for neighbor, weight in graph[node]:
            if neighbor not in distances:
                hq.heappush(heap, (dist + weight, neighbor))

    return distances
        
    
import sys
  
[n,m,s,t,k] = list(map(int, sys.stdin.readline().strip().split()))

g = {}
    
for j in range(m):
    [u,v,w]  = list(map(int, sys.stdin.readline().strip().split()))
    if u in g:
        g[u].append((v,w))
    else:
        g[u] = [(v,w)]

    if v in g:
        g[v].append((u,w))
    else:
        g[v] = [(u,w)]

guardians = list(map(int, sys.stdin.readline().strip().split()))
D = dijkstra(g, t)
min_dis = float("inf")
for gu in guardians:
    if D[gu]<min_dis:
        min_dis = D[gu]

harry_dis = D[s]
if (harry_dis>=min_dis):
    print("impossible")
else:
    print(harry_dis)
