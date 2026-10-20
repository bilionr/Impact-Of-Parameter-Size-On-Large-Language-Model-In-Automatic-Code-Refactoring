from collections import deque

n = int(input())

la = [[] for i in range(n)]


for _ in range(n):
    lb = list(map(int, input().split()))
    i = lb[0]
    if lb[1] != 0:
        lb = list(map(lambda x: x - 1, lb[2:]))
        la[i - 1] = lb.copy()


lc = [[-1, -1] for j in range(n)]
cnt = 0


def dfs(p):
    global cnt
    cnt += 1
    lc[p][0] = cnt
    for a in la[p]:
        if lc[a][0] == -1:
            dfs(a)
    cnt += 1
    lc[p][1] = cnt


for i in range(n):
    if lc[i][0] == -1:
        dfs(i)

for i in range(n):
    print(i + 1, lc[i][0], lc[i][1])

