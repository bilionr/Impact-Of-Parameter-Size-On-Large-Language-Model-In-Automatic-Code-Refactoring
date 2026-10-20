import sys, math
from operator import itemgetter
from bisect import bisect_left, bisect_right

f_i = sys.stdin

def main():
    n = int(f_i.readline())
    
    lx = []
    ly = []
    li = []
    for i in range(n):
        x, y = map(int, f_i.readline().split())
        lx.append(x)
        ly.append(y)
        li.append(i)

    x_width = max(lx) - min(lx)
    y_width = max(ly) - min(ly)
    if x_width > y_width:
        P = list(zip(lx, ly, li))
    else:
        P = list(zip(ly, lx, li))
    P.sort()

    interval = int(math.sqrt(n))

    low = [v1 for v1, v2, i in P[::interval]]
    high = [v1 for v1, v2, i in P[interval - 1::interval]] + [float('inf')]

    S = []
    v2_sec_list = []
    for i in range(0, n, interval):
        si = P[i:i + interval]
        si.sort(key=itemgetter(1))
        v2_s = [p[1] for p in si]
        v2_sec_list.append(v2_s)
        S.append(si)

    A = []

    q = f_i.readline()

    for l in f_i:
        sx, tx, sy, ty = map(int, l.split())
        a = []
        if x_width > y_width:
            for i in range(bisect_left(high, sx), bisect_right(low, tx)):
                v = S[i]
                k = v2_sec_list[i]
                for j in range(bisect_left(k, sy), bisect_right(k, ty)):
                    if sx <= v[j][0] <= tx:
                        a.append(v[j][2])
        else:
            for i in range(bisect_left(high, sy), bisect_right(low, ty)):
                v = S[i]
                k = v2_sec_list[i]
                for j in range(bisect_left(k, sx), bisect_right(k, tx)):
                    if sy <= v[j][0] <= ty:
                        a.append(v[j][2])
        
        if a:
            a.sort()
            A.extend(a)
        A.append('')

    print('\n'.join(map(str, A)))

main()
