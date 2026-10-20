# aizu_DPL_5_I_Balls&Boxes9.py  
# Stirling Number

MOD = 10**9+7
n,k = map(int,input().split())

fact = [1,1]
factinv = [1, 1] 
inv = [0, 1] 
for i in range(2, k + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

def comb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    return fact[n] * factinv[r] * factinv[n-r] % p

def zensya(n,k):
    ans = 0
    sign = -1
    for i in range(k,0,-1):
        sign *= -1
        t = sign*comb(k,i,MOD)*pow(i,n,MOD) % MOD
        ans += t
        ans %= MOD
    return ans

def stirling(n,k):
    ans = zensya(n,k)*factinv[k] % MOD
    return ans

print(stirling(n,k))
