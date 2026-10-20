import math

n = int(input())
x = [int(s) for s in input().split()]
y = [int(s) for s in input().split()]
for p in range(1, 4):
    d = (sum([abs(x[i] - y[i]) ** p for i in range(n)])) ** (1 / p)
    print("{:.6f}".format(float(d)))
d = max([abs(x[i] - y[i]) for i in range(n)])
print("{:.6f}".format(float(d)))

