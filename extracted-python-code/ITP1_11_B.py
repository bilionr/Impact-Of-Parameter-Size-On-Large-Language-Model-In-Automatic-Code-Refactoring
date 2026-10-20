dice = [int(s) for s in input().split()]
n = int(input())
# data[i]の中の隣り合う数字は、デフォルトさいころについて、右面がiであるときの上面と前面の組み合わせ。
data = [
    [1, 2, 4, 3, 1],
    [0, 3, 5, 2, 0],
    [0, 1, 5, 4, 0],
    [0, 4, 5, 1, 0],
    [0, 2, 5, 3, 0],
    [1, 3, 4, 2, 1],
    ]
for i in range(n):
    t, f = map(int, input().split())
    found = 0
    for j in range(6):
        for k in range(4):
            if dice[data[j][k]] == t and dice[data[j][k + 1]] == f:
                print(dice[j])
                found= 1
                break
        if found:
            break
