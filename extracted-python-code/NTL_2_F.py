from decimal import *
a, b = input().split()
getcontext().prec = len(a)+len(b)
ans = Decimal(a)*Decimal(b)
if ans == 0:
    print(0)
else:
    print(ans)
