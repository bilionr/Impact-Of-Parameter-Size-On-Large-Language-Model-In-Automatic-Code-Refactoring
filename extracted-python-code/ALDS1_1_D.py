import sys
a=1e10
b=-a
input()
for i in map(int,sys.stdin):
    if b<i-a:b=i-a
    if a>i:a=i
print(b)
