from heapq import heappush, heappop

INFTY = float('inf')

def dijkstra(n, adj_list):
    d = [INFTY] * n
    d[0] = 0
    pque = [(0, 0)]

    while pque:
        dist_u, u = heappop(pque)
        if d[u] < dist_u:
            continue
        for i in range(0, len(adj_list[u]), 2):
            v, weight = adj_list[u][i], adj_list[u][i+1]
            new_dist = d[u] + weight
            if new_dist < d[v]:
                d[v] = new_dist
                heappush(pque, (new_dist, v))
    return d

n = int(input())
adj_list = [list(map(int, input().split()))[2:] for _ in range(n)]
result = dijkstra(n, adj_list)
print("\n".join(f"{i} {dist}" for i, dist in enumerate(result)))

