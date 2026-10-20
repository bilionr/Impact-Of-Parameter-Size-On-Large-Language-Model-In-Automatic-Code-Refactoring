def solve(h:int,w:int,g:list[list[int]]) -> int:
    dp = [0] * (w + 1)

    max_size = 0
    for i in range(1,h+1):
        next_dp = [0] * (w + 1)
        for j in range(1,w+1):
            if g[i-1][j-1] == 1:
                next_dp[j] = 0
            else:
                dp_value = min(dp[j-1],dp[j],next_dp[j-1]) + 1
                next_dp[j] = dp_value
                max_size = max(max_size,dp_value)
        dp = next_dp
    
    return max_size ** 2

if __name__ == '__main__':
    h,w = list(map(int,input().split()))
    g = []
    for _ in range(h):
        g.append(list(map(int,input().split())))

    print(solve(h,w,g))

