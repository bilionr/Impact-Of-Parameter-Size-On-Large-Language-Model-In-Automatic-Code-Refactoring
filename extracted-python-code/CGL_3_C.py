def inside_polygon(p0, qs):
    cnt = 0
    L = len(qs)
    x, y = p0
    for i in range(L):
        x0, y0 = qs[i-1]; x1, y1 = qs[i]
        x0 -= x; y0 -= y
        x1 -= x; y1 -= y

        cv = x0*x1 + y0*y1
        sv = x0*y1 - x1*y0
        if sv == 0 and cv <= 0:
            return 1

        if not y0 < y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        if y0 <= 0 < y1 and x0*(y1 - y0) > y0*(x1 - x0):
            cnt += 1
    return 2 if cnt % 2 == 1 else 0

def solve():
    N = int(input())
    qs = [list(map(int, input().split())) for i in range(N)]

    Q = int(input())
    for i in range(Q):
        *p0, = map(int, input().split())
        print(inside_polygon(p0, qs))
solve()
