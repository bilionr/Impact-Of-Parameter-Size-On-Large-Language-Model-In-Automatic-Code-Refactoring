import sys
sys.setrecursionlimit(200000)

def main():
    input = sys.stdin.read
    data = input().split()

    V, E = int(data[0]), int(data[1])
    graph = [[] for _ in range(V)]
    idx = 2
    for _ in range(E):
        a, b = int(data[idx]), int(data[idx+1])
        idx += 2
        graph[a].append(b)
        graph[b].append(a)

    ord = [-1] * V
    low = [0] * V
    bridges = []
    time = 0

    def dfs(v, parent):
        nonlocal time
        ord[v] = low[v] = time
        time += 1

        for to in graph[v]:
            if ord[to] == -1:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if ord[v] < low[to]:
                    bridges.append((min(v, to), max(v, to)))
            elif to != parent:
                low[v] = min(low[v], ord[to])

    dfs(0, -1)

    bridges.sort()
    for u, v in bridges:
        print(u, v)

if __name__ == "__main__":
    main()

