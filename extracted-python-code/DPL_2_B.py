import sys

INF = float('inf')
input = sys.stdin.readline
V, E = map(int, input().split())

# floyd warshall teoria de grafos
#何をしているのか: 全頂点間の最短距離を計算する、非常に効率的なアルゴリズムを使っています。
#目的: 奇数次数の頂点間の最短経路を後で利用するために、距離行列を完全に初期化。
def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

adj = [[] for _ in range(V)]
deg = [0] * V
base_cost = 0

dist = [[INF] * V for _ in range(V)]
for i in range(V):
    dist[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    deg[u] += 1
    deg[v] += 1
    base_cost += w
    if dist[u][v] > w:
        dist[u][v] = w
        dist[v][u] = w

dist = floyd_warshall(V, dist)

# impares
#奇数次数の頂点のリストアップoddの１行
#何をしているのか: 各頂点の次数を計算し、その中から奇数次数の頂点を抽出。
#目的: 奇数次数の頂点はペアリングして閉路を作るために必要なので、これを管理する。
odd_vertices = [i for i in range(V) if deg[i] % 2 == 1]
m = len(odd_vertices)
#状態管理を用いた動的計画法（DP）
#何をしているのか: 奇数頂点のペアリング問題をビットマスクを用いて効率的に探索。
#目的: すべての奇数次数の頂点をペアにする最小コストを求める。
dp = [INF] * (1 << m)
dp[0] = 0

for mask in range(1 << m):
    if dp[mask] == INF:
        continue
    for i in range(m):
        if not (mask & (1 << i)):
            for j in range(i + 1, m):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << i) | (1 << j)
                    cost = dist[odd_vertices[i]][odd_vertices[j]]
                    if dp[new_mask] > dp[mask] + cost:
                        dp[new_mask] = dp[mask] + cost
            break

min_additional_cost = dp[(1 << m) - 1]

#何をしているのか: 元のグラフの辺のコスト（base_cost）と、奇数次数頂点のペアリングに必要な追加コスト（min_additional_cost）を合計して、最短閉路の距離を出力。
#目的: 問題の解を求める。
total_cost = base_cost + min_additional_cost
print(total_cost)



