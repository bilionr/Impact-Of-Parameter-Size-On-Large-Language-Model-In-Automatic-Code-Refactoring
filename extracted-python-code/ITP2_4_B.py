n = int(input())
A = list(map(int, input().split()))
q = int(input())
results = []
for _ in range(q):
    Q = list(map(int, input().split()))
    A[Q[0]:Q[2]] = A[Q[1]:Q[2]] + A[Q[0]:Q[1]]

print(" ".join(map(str, A)))
