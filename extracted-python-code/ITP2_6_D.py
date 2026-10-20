import bisect
import sys

read = sys.stdin.readline
write = sys.stdout.write

n = int(read())
a = list(map(int, read().split()))
q = int(read())
output = ""

for _ in range(q):
    k = int(read())
    lower = bisect.bisect_left(a, k)
    upper = bisect.bisect_right(a, k)
    output += f"{lower} {upper}\n"

write(output)

