def main() -> None:
    import sys
    from heapq import heappush, heappop

    input = sys.stdin.readline
    v_num, e_num, r = map(int, input().split())
    G = [[] for _ in range(v_num)]
    for _ in range(e_num):
        s, t, d = map(int, input().split())
        G[s].append((t, d))

    INF: int = 1 << 60
    dist = [INF] * v_num
    dist[r] = 0
    heap = []
    heappush(heap, (0, r))

    while heap:
        cd, cv = heappop(heap)
        if dist[cv] < cd:
            continue
        for nv, d in G[cv]:
            if dist[nv] > dist[cv] + d:
                dist[nv] = dist[cv] + d
                heappush(heap, (dist[nv], nv))

    for d in dist:
        if d == INF:
            print("INF")
        else:
            print(d)


if __name__ == "__main__":
    main()

