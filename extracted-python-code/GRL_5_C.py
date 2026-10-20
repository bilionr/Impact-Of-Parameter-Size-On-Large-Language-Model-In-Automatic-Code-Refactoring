import sys
sys.setrecursionlimit(10**6)

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
G = [None]*N
for v in range(N):
    k, *G[v] = map(int, readline().split())

Q = int(readline())
QS = [tuple(map(int, readline().split())) for i in range(Q)]

def lca(N, G, s, QS):
    res = [-1]*len(QS)

    A = [[] for i in range(N)]
    for i, (u, v) in enumerate(QS):
        if u == v:
            res[i] = u
            continue
        A[u].append((v, i))
        A[v].append((u, i))

    *prt, = range(N)
    def root(x):
        if x == prt[x]:
            return x
        prt[x] = x = root(prt[x])
        return x
    def unite(x, y):
        px = root(x); py = root(y)
        if px < py:
            prt[py] = px
            return px
        else:
            prt[px] = py
            return py

    anc = [-1]*N

    stk = [s]
    it = [0]*N
    while stk:
        v = stk[-1]
        if it[v] == 0:
            anc[v] = v
        else:
            anc[unite(v, G[v][it[v]-1])] = v

        if it[v] < len(G[v]):
            stk.append(G[v][it[v]])
            it[v] += 1
        else:
            pv = root(v)
            for w, i in A[v]:
                if anc[w] != -1 and pv != root(w):
                    res[i] = anc[root(w)]
            stk.pop()
    return res

ans = lca(N, G, 0, QS)
write("\n".join(map(str, ans)))
write("\n")

