import sys
readline = sys.stdin.readline
write = sys.stdout.write

from itertools import repeat

N = int(readline())
L = 10001

C = [0]*L;
for a in map(int, readline().split()):
    C[a] += 1


ans = []
for i, c in enumerate(C):
    if c:
        ans.extend(repeat(str(i), c))
write(" ".join(ans))
write("\n")

