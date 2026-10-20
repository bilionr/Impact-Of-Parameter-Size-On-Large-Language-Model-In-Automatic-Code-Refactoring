import math
def count(N):
    p = int(math.log2(N))
    q = N - 2**p
    return (p*(2**p)+(p+2)*q)
    
N = int(input())
L = list(map(int,input().split()))

print(' '.join(list(map(str,sorted(L)))))
print(count(N))
