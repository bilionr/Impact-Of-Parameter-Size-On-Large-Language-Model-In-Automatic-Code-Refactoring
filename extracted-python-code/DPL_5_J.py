def p_bell(n, k):
    MOD = 10**9 + 7
    # DPテーブルの初期化
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # 初期条件

    for i in range(1, n + 1):
        for j in range(1, k + 1):
          if i >= j:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - j][j]) % MOD
    
    ans = 0
    for j in range(k + 1):
        ans += dp[n][j]
        if ans > MOD:
            ans %= MOD
    
    return ans

n, k = map(int, input().split())

print(p_bell(n, k))
