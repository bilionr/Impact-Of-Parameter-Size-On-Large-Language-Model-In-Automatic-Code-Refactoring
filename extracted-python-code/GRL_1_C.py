import sys
readline = sys.stdin.readline
writelines = sys.stdout.writelines
write = sys.stdout.write

from collections import deque
from heapq import heappush, heappop

INF = 10**30
def Johnson(G):
    h = [0]*N

    update = 1
    for i in range(N):
        update = 0
        for v in range(N):
            d = h[v]
            for w, c in G[v]:
                if c + d < h[w]:
                    h[w] = d + c
                    update = 1
        if not update:
            break
    else:
        return None

    for v in range(N):
        d = h[v]
        g = G[v]
        for j, (w, c) in enumerate(g):
            g[j] = (w, c + d - h[w])

    D = []
    for i in range(N):
        dst = [INF]*N
        dst[i] = 0
        que = [(0, i)]
        while que:
            cost, v = heappop(que)
            if dst[v] < cost:
                continue
            for w, c in G[v]:
                if cost + c < dst[w]:
                    dst[w] = r = cost + c
                    heappush(que, (r, w))
        v = h[i]
        for j in range(N):
            if dst[j] == INF:
                dst[j] = INF
            else:
                dst[j] -= v - h[j]
        D.append(dst)

    return D


N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    s, t, d = map(int, input().split())
    G[s].append((t, d))

D = Johnson(G)
if D:
    ans = []
    for i in range(N):
        ans.append(" ".join(str(v) if v < INF else "INF" for v in D[i]))
        ans.append("\n")
    writelines(ans)
else:
    write("NEGATIVE CYCLE\n")


