# 最長増加部分列
# 解答閲覧


import sys
import bisect

input = sys.stdin.readline


def main():

    n = int(input())
    A = [int(input()) for _ in range(n)]
    INF = float('inf')
    dp = [INF]*(n+1)

    for i in range(n):
        index = bisect.bisect_left(dp,A[i])
        dp[index] = A[i]
    
    ans = 0
    for i in range(n+1):
        if dp[i] == INF:
            break
        else:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()




