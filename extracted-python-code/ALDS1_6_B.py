def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

n = int(input())
A = list(map(int, input().split()))
q = partition(A, 0, n-1)
print(' '.join(map(str, A[:q])), end=' ')
print(f"[{A[q]}]", end=' ')
print(' '.join(map(str, A[q+1:])))

