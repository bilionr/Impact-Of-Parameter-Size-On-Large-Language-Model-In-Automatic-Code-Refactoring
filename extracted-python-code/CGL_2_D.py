def dot(a, b):
    return (a.conjugate() * b).real
def cross(a, b):
    return (a.conjugate() * b).imag
def ccw(a, b, c):
    return cross(b - a, c - a) > 0

def intersect(a1, a2, b1, b2):
    return (ccw(a1,b1,b2) != ccw(a2,b1,b2)) and (ccw(a1,a2,b1) != ccw(a1,a2,b2))

def distancelp(p0, p1, p):
    l = p1 - p0
    return abs(cross(p - p0,l)) / abs(l)

def distancesp(a, b, p):
    if dot(b - a, p - a) < 0.0:
        return abs(p - a)
    if dot(a - b, p - b) < 0.0:
        return abs(p - b)
    return distancelp(a, b, p)
    

def solve():
    q = int(input())
    for _ in range(q):
        x0, y0, x1,y1,x2,y2,x3,y3 = map(float, input().split())
        p0 = complex(x0, y0)
        p1 = complex(x1, y1)
        p2 = complex(x2, y2)
        p3 = complex(x3, y3)
        ans = 0
        if intersect(p0, p1, p2, p3):
            ans = 0.0
        else:
            ans = min(distancesp(p0, p1, p2), distancesp(p0, p1, p3), distancesp(p2, p3, p0), distancesp(p2, p3, p1))
        print(f'{ans:.10f}')


solve()
