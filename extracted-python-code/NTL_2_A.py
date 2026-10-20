from decimal import *

a, b= input().rstrip().split(' ')

# num_len = max(len(a), len(b)) + 1
# minprec = 27
# if num_len > minprec:
#     getcontext().prec = num_len
# else:
#     getcontext().prec = minprec
getcontext().prec = 1000000    

print(Decimal(a) + Decimal(b))
