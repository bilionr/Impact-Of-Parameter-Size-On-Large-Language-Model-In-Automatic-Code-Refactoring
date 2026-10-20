n, k = map(int, input().split())

if n < k:
    print(0)

elif n == k:
    print(1)

else:

    n = n - k

    mod = 10 ** 9 + 7


    dp = [[0] * (k + 1) for i in range(n+ 1)]

    for j in range(k + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i][j-1]

            if i >= j:
                dp[i][j] = (dp[i][j] + dp[i-j][j]) % mod

    print(dp[n][k])


