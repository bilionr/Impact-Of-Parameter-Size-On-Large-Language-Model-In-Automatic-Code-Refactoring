from collections import deque
import sys
input = sys.stdin.readline

n,q = map(int,input().split())
S = [deque() for i in range(n)]
for i in range(q):
    queue = list(input().split())
    p = queue[0]
    t = int(queue[1])
    if p == "0":
        r = int(queue[2])
        S[t].append(r)
    elif p == "1":
        print(" ".join(map(str,S[t])))
    else:
        r = int(queue[2])
        if S[r]:
            if len(S[t]) == 1:
                S[r].append(S[t][0])
            elif len(S[r]) == 1:
                S[t].appendleft(S[r][0])
                S[r] = S[t]
            elif len(S[t]) >= 2:
                S[r] += S[t]
        else:
            S[r] = S[t]
        S[t] = deque()
