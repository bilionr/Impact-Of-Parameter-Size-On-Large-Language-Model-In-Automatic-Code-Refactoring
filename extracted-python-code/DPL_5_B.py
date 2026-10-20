import sys
input = lambda: sys.stdin.readline().rstrip()
MOD=10**9+7
# これはkPn通り

N,K=map(int,input().split())
res=1

while N:
    res*=K
    res%=MOD
    N-=1
    K-=1


print(res)
