N = int(input())
L = list(map(int,input().split()))
count = 0
for n in range(N):
    while n > 0 and L[n] < L[n-1]:
        L[n],L[n-1] = L[n-1],L[n]
        count += 1
        n -= 1

L = list(map(str,L))        
print(' '.join(L))
print(count)
        
