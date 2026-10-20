import sys
from collections import deque
input = sys.stdin.read
n,*q=input().splitlines()
a=deque()
for query in q:
    o=query.split()
    if o[0]=="0":
        if o[1]=="0":
            a.appendleft(int(o[2]))
        elif o[1]=="1":
            a.append(int(o[2]))
    elif o[0]=="1":
        print(a[int(o[1])])
    elif o[0]=="2":
        if o[1]=="0":
            a.popleft()
        elif o[1]=="1":
            a.pop()
