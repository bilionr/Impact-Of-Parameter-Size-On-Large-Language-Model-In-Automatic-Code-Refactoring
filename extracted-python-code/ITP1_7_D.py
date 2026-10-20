n, m, t = map(int, input().split())

A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(m)]
B_ = [list(i) for i in zip(*B)]  # 転置行列

for i in range(n):
    ans = []
    for j in range(t):
        ans.append(sum([x*y for (x, y) in zip(A[i], B_[j])]))   
    print(*ans)
