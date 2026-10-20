import sys
input = lambda: sys.stdin.readline().rstrip()
MOD=10**9+7
sys.setrecursionlimit(10**8)

# 難しい

##n以下の階乗とそのmod逆元を作る
def modfact(n):

    fact[0]=1
    invfact[0]=1
    
    for i in range(n):
        fact[i+1]=((i+1)*fact[i])%MOD
        invfact[i+1]=pow(fact[i+1],MOD-2,MOD)
    


##modを取った組合せを計算する
def modcomb(n,r):

    if r<=0 or n<r:return 0

    ret=0
    ret=(fact[n]*invfact[r])%MOD
    ret=(ret*invfact[n-r])%MOD

    return ret

N,K=map(int,input().split())

# 箱の方が多ければ実現不能
if N<K:
    print(0)
    exit(0)


fact=[0]*(N+1)
invfact=[0]*(N+1)

modfact(N)


# まず何も考えずN個のボールをK個の箱に入れる場合の数を考える
# これはK**N通り
res=pow(K,N,MOD)

# K箱中i箱空にする場合の数
def f(i):
    if i==K:return 0
    return (modcomb(K,i)*pow(K-i,N,MOD)-f(i+1))%MOD

print((res-f(1))%MOD)
