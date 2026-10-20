import math

while True:
    n = int(input())
    if n == 0:
        break
    scores = [int(s) for s in input().split()]
    m = sum(scores) / n
    v = sum([(i - m) ** 2 for i in scores]) / n
    sd = math.sqrt(v)
    print("{:.4f}".format(sd))
