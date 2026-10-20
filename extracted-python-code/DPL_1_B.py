import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    N = int(next(it))
    W = int(next(it))

    dp = [0] * (W + 1)

    for _ in range(N):
        v = int(next(it))
        w = int(next(it))

        # 0/1 knapsack: go backward so each item used at most once
        for cap in range(W, w - 1, -1):
            candidate = dp[cap - w] + v
            if candidate > dp[cap]:
                dp[cap] = candidate

    print(dp[W])

if __name__ == "__main__":
    main()
