def selectionsort(A,N):
    ans =0
    for i in range(N-1):
        minj = i
        for j in range(i,N):
            if A[j]<A[minj]:
                minj = j
        if i != minj:
            A[i],A[minj]=A[minj],A[i]
            ans += 1
    print(*A)
    print(ans)
N = int(input())
A = list(map(int,input().split()))
selectionsort(A,N)

