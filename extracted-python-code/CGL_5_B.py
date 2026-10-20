import sys
import math
import random


def inside(circle,p):
    """点p=(x,y)がcircle(cx,cy,r)の内部にあるか"""
    cx,cy,r = circle
    dx = p[0] -cx
    dy = p[1] -cy
    return dx*dx +dy*dy <= r*r + 1e-12

def circle_2(a,b):
    """2点a,bを直径の両端とする円"""
    x1,y1 = a
    x2,y2 = b
    cx = (x1+x2) / 2.0
    cy = (y1+y2) / 2.0
    r = math.hypot(x1 - x2, y1 - y2) / 2.0
    return (cx,cy,r)

def circle_3(a,b,c):
    """3点 a,b,c を境界とする円（外接円）"""
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    d = 2.0 * (x1*(y2 -y3)+ x2*(y3-y1)+ x3*(y1-y2))
    if abs(d) < 1e-12:
        return (0.0,0.0,float('inf'))
    ux = ((x1*x1 + y1*y1)*(y2-y3)+(x2*x2 + y2*y2)*(y3-y1)+(x3*x3 + y3*y3)*(y1-y2)) / d
    uy = ((x1*x1 + y1*y1)*(x3-x2)+(x2*x2 + y2*y2)*(x1-x3)+(x3*x3 + y3*y3)*(x2-x1)) / d    
    r = math.hypot(ux - x1,uy - y1)
    return (ux,uy,r)

def make_circle(points):
    """
    1.ランダムにシャッフル
    2.順に点を追加。もし既存の円に含まれなければさらに更新
    """
    P = points[:]
    random.seed(42)
    random.shuffle(P)
    C = None
    for i,p in enumerate(P):
        if C is None or not inside(C,p):
            C = (p[0],p[1],0.0)
            for j in range(i):
                q = P[j]
                if not inside(C,q):
                    C = circle_2(p,q)
                    for k in range(j):
                        r_pt = P [k]
                        if not inside(C,r_pt):
                            C = circle_3(p,q,r_pt)
    return C                        


def main():    
    input = sys.stdin.readline
    n = int(input())
    pts = [tuple(map(float,input().split())) for _ in range(n)]
    cx,cy,r =make_circle(pts)
    print(f"{cx:.8f} {cy:.8f} {r:.8f}")

if __name__ == "__main__":
    main()               

