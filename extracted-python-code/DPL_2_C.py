import sys

# READ_FROM_FILE = True
READ_FROM_FILE = False


def main():
    if READ_FROM_FILE:
        f = open('test0.txt', 'r')
    else:
        f = sys.stdin

    n = int(f.readline())
    p_list = []
    for _ in range(n):
        x, y = map(int, f.readline().split())
        p_list.append(complex(x, y))

    d_list = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            v = p_list[i] - p_list[j]
            d_list[i][j] = abs(v)
            d_list[j][i] = d_list[i][j]

    dp = [[0.0] * n for _ in range(n)]
    for j in range(1, n):
        for i in range(j):
            if i == 0 and j == 1:
                dp[i][j] = d_list[i][j]
            elif i < j - 1:
                dp[i][j] = dp[i][j - 1] + d_list[j - 1][j]
            else:
                dp[i][j] = float('inf')
                for k in range(i):
                    dp[i][j] = min(dp[i][j], dp[k][i] + d_list[k][j])

    result = float('inf')
    for k in range(n - 1):
        result = min(result, dp[k][n - 1] + d_list[k][n - 1])

    print(f'{result:.4f}')

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == '__main__':
    main()

