from collections import deque
def bfs(graph, start=0):
    dist = [-1]*len(graph)
    dist[start] = 0
    q = deque([start])
    while q:
        curr = q.popleft()
        for adj, d in graph[curr]:
            if dist[adj]!=-1:
                continue
            dist[adj] = dist[curr]+d
            q.append(adj)
    return dist

def tree_height(graph):
    d0 = bfs(graph)
    idx1 = d0.index(max(d0))
    d1 = bfs(graph, idx1)
    idx2 = d1.index(max(d1))
    d2 = bfs(graph, idx2)
    return [max(d1[i], d2[i]) for i in range(len(graph))]

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
print(*tree_height(g), sep="\n")
