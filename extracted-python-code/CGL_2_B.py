# aizu_CGL_2_B_Intersection.py 交点判定
def dot_p(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)

def cross_p(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)

def dist(A, B):
    ax, ay = A; bx, by = B
    return (ax - bx) ** 2 + (ay - by) ** 2

def is_intersection(P0, P1, Q0, Q1):
    C0 = cross_p(P0, P1, Q0)
    C1 = cross_p(P0, P1, Q1)
    D0 = cross_p(Q0, Q1, P0)
    D1 = cross_p(Q0, Q1, P1)
    if C0 == C1 == 0:
        E0 = dot_p(P0, P1, Q0)
        E1 = dot_p(P0, P1, Q1)
        if not E0 < E1:
            E0, E1 = E1, E0
        return E0 <= dist(P0, P1) and 0 <= E1
    return C0 * C1 <= 0 and D0 * D1 <= 0

q = int(input())
for _ in range(q):
    point = list(map(int,input().split()))
    P0 = point[0:2]
    P1 = point[2:4]

    Q0 = point[4:6]
    Q1 = point[6:8]

    ans = is_intersection(P0, P1, Q0, Q1)
    print(int(ans))
