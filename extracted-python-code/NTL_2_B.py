from decimal import *

a, b = input().rstrip().split(' ')

getcontext().prec = 100001 

print(Decimal(a) - Decimal(b))
