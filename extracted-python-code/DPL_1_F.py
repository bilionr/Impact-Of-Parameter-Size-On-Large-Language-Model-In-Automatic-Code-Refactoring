INF = 10**15


def solve_small_value_knapsack_problem_1D(
    N: int,
    W: int,
    items: list[tuple[int, int]],
) -> int:
    """価値の総和が小さい0-1ナップザック問題を1次元配列のDPで解く

    Args:
        N (int): アイテム数
        W (int): 容量制約
        items (list[tuple[int, int]]): 各アイテムの(重み, 価値)

    Returns:
        int: 最適化の価値のmax (-INFの場合, 実行可能解は存在しない)
    """
    sum_V = sum(v for _, v in items)

    DP = [INF] * (sum_V + 1)
    DP[0] = 0

    for i in range(1, N + 1):
        wi, vi = items[i - 1]
        # vが小さい方 -> 大きい方という遷移を行うので,
        # 上書きしないように, vを大きい方から遷移していく必要がある
        for v in range(sum_V + 1)[::-1]:
            # i番目の品物を使う場合
            if (DP[v] < INF) and (v + vi <= sum_V):
                DP[v + vi] = min(DP[v + vi], DP[v] + wi)

            # 使わない場合は現在の配列に既に答えがはいっている

    return max(v for v in range(sum_V + 1) if DP[v] <= W)



N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w = map(int, input().split())
    items.append((w, v))

print(solve_small_value_knapsack_problem_1D(N, W, items))
