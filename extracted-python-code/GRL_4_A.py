# 有向グラフの閉路検査


import sys

sys.setrecursionlimit(100000)


def dfs(G,v,seen,finished):
    seen[v] = True

    for to in G[v]:
        if finished[to] == True:
            continue
        if seen[to] != finished[to]:
            return True
        
        if dfs(G,to,seen,finished):
            return True
        
    finished[v] = True

    return False


def main():

    V,E = map(int, input().split())

    G = [[] for _ in range(V)]

    for i in range(E):
        s,t = map(int, input().split())
        G[s].append(t)
    
    seen = [False]*V
    finished = [False]*V
    ans = 0
    for i in range(V):
        if seen[i] == True:
            continue
        if dfs(G,i,seen,finished):
            print(1)
            exit()
    print(ans)


if __name__ == '__main__':
    main()
    
