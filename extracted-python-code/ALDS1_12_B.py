import heapq
n = int(input())
G = [[] for _ in range(n)]
d = [float('inf')]*n # the distance form 0 to v

def dijkstra(start):
    que = []
    d[0] = 0
    heapq.heappush(que, (0, start))
    while que:
        cur_dist_from_start, cur_node = heapq.heappop(que)
        if cur_dist_from_start > d[cur_node]:
            continue
        for next_node, edge_weight in G[cur_node]:
            dist_to_next_node = d[cur_node] + edge_weight
            if d[next_node] > dist_to_next_node:
                d[next_node] = dist_to_next_node
                heapq.heappush(que, (dist_to_next_node, next_node))
    return d

def main():
    for _ in range(n):
        table = list(map(int, input().split()))
        for i in range(table[1]):
            G[table[0]].append((table[2+2*i], table[3+2*i]))
    dijkstra(0)
    for i in range(n):
        print(i, d[i])
    


if __name__ == '__main__':
    main()
