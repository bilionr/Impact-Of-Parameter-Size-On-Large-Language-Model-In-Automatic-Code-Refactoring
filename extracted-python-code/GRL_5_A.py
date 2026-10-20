from collections import deque
from math import inf
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        s, t, w = map(int, input().split())
        g[s].append((t, w))
        g[t].append((s, w))
    
    def dfs(x):
        dis = [inf] * n
        dis[x] = 0
        q = deque([x])
        while q:
            u = q.popleft()
            for v, c in g[u]:
                if dis[v] == inf:
                    dis[v] = dis[u] + c
                    q.append(v)
        return dis
    
    res1 = dfs(0)
    tgt = max(range(n), key = lambda i: res1[i])
    res2 = dfs(tgt)
    print(max(res2))
    
main()
