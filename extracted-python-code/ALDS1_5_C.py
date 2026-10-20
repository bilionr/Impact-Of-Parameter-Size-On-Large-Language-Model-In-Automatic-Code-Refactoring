import math

def vertices(n, i, p, q):
    if n == 0:
        return [(q)]
    a = 100 / 3 ** (i + 1)
    s = ((2 * p[0] + q[0]) / 3, (2 * p[1] + q[1]) / 3)
    t = ((p[0] + 2 * q[0]) / 3, (p[1] + 2 * q[1]) / 3)
    if p[0] < q[0]:
        if p[1] < q[1]:
            u = (t[0] - a, t[1])
        elif p[1] == q[1]:
            u = ((s[0] + t[0]) / 2, s[1] + a * math.sqrt(3) / 2)
        else:
            u = (s[0] + a, s[1])
    else:
        if p[1] < q[1]:
            u = (s[0] - a, s[1])
        elif p[1] == q[1]:
            u = ((s[0] + t[0]) / 2, s[1] - a * math.sqrt(3) / 2)
        else:
            u = (t[0] + a, t[1])
    if i == n - 1:
        return [s, u, t, q]
    return vertices(n, i + 1, p, s) + vertices(n, i + 1, s, u) + vertices(n, i + 1, u, t) + vertices(n, i + 1, t, q)

n = int(input())
print("{:.8f} {:.8f}".format(0, 0))
for v in vertices(n, 0, (0, 0), (100, 0)):
    print("{:.8f} {:.8f}".format(v[0], v[1]))
