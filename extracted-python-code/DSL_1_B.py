import sys
readline = sys.stdin.readline
write = sys.stdout.write

N, Q = map(int, readline().split())
*p, = range(N)
data = [0]*N
def root(x):
    if x == p[x]:
        return x
    r = p[x]
    p[x] = y = root(r)
    data[x] += data[r]

    return y
def unite(x, y, z):
    px = root(x); py = root(y)
    if px == py:
        return 0
    if px < py:
        p[py] = px
        data[py] = data[x] - data[y] - z
    else:
        p[px] = py
        data[px] = data[y] - data[x] + z
    return 1


ans = []
for q in range(Q):
    t, *cmd = map(int, readline().split())
    if t:
        x, y = cmd
        px = root(x); py = root(y)
        if px == py:
            ans.append(str(data[x] - data[y]))
        else:
            ans.append("?")
    else:
        x, y, z = cmd
        unite(x, y, z)
write("\n".join(ans))
write("\n")


