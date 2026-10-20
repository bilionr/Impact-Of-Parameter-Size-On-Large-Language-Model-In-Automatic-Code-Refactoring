# aizu_DPL_5_E_Balls&Boxes5.py  
# ball:区別なしn個　　box:区別ありk個 箱の中のバールは1個まで

MOD = 10**9+7
n,k = map(int,input().split())

fact = [1,1]
factinv = [1, 1] 
inv = [0, 1] 
for i in range(2, n + k ):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

def comb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    return fact[n] * factinv[r] * factinv[n-r] % p

ans = comb(k,n,MOD)
print(ans)
