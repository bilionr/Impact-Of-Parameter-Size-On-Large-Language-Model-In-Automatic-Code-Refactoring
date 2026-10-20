# aizu_DPL_4_CoinCombinationProblem.py

from itertools import product
from collections import Counter

N,V = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))

ab = [ aa+bb for aa,bb in product(a,b)]
c_x = Counter(ab)
cd = [ cc+dd for cc,dd in product(c,d)]
c_y = Counter(cd)

ans = 0
for w,x in c_x.items():
    target = V-w
    y = c_y[target]
    ans += x*y
print(ans)
