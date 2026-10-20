import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    *A, = map(int, readline().split())
    A.sort()
    for i in range(N-1):
        j = i
        while j > 0:
            k = (j - 1) // 2
            A[j], A[k] = A[k], A[j]
            j = k
        A[0], A[i+1] = A[i+1], A[0]
    write(" ".join(map(str, A)))
    write("\n")
solve()
