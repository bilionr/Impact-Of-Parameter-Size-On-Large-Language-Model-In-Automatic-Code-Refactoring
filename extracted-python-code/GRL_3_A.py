from collections import defaultdict
import sys
sys.setrecursionlimit(200000)

def find_articulation_points(V, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    discovery_time = [-1] * V
    low = [-1] * V
    parent = [-1] * V
    articulation_points = set()
    time = [0]

    def dfs(u):
        discovery_time[u] = low[u] = time[0]
        time[0] += 1
        children = 0

        for v in graph[u]:
            if discovery_time[v] == -1:  # v is not visited
                parent[v] = u
                children += 1
                dfs(v)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    articulation_points.add(u)
                if parent[u] != -1 and low[v] >= discovery_time[u]:
                    articulation_points.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], discovery_time[v])

    for i in range(V):
        if discovery_time[i] == -1:
            dfs(i)

    return sorted(articulation_points)

def main():
    input = sys.stdin.read
    data = input().split()
    
    V = int(data[0])
    E = int(data[1])
    edges = []
    
    index = 2
    for _ in range(E):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    articulation_points = find_articulation_points(V, edges)
    for ap in articulation_points:
        print(ap)

if __name__ == "__main__":
    main()

