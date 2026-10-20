import sys
sys.setrecursionlimit(200000)

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    V, E = int(data[idx]), int(data[idx+1])
    idx += 2

    G = [[] for _ in range(V)]
    rG = [[] for _ in range(V)]
    for _ in range(E):
        s, t = int(data[idx]), int(data[idx+1])
        G[s].append(t)
        rG[t].append(s)
        idx += 2

    # Kosaraju’s algorithm
    visited = [False] * V
    order = []

    def dfs(v):
        visited[v] = True
        for to in G[v]:
            if not visited[to]:
                dfs(to)
        order.append(v)

    def rdfs(v, k):
        group[v] = k
        visited[v] = True
        for to in rG[v]:
            if not visited[to]:
                rdfs(to, k)

    for v in range(V):
        if not visited[v]:
            dfs(v)

    visited = [False] * V
    group = [-1] * V
    k = 0
    for v in reversed(order):
        if not visited[v]:
            rdfs(v, k)
            k += 1

    # Queries
    Q = int(data[idx])
    idx += 1
    output = []
    for _ in range(Q):
        u, v = int(data[idx]), int(data[idx+1])
        idx += 2
        if group[u] == group[v]:
            output.append("1")
        else:
            output.append("0")

    print("\n".join(output))

if __name__ == "__main__":
    main()

