from math import *
EPS=10**(-8)
def equal(a,b):
    if abs(a-b)<EPS:
        return True
    else:
        return False

class point:                 
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __neg__(self):
        return point(-self.x,-self.y)
    def __pos__(self):
        return self
    def __eq__(self,other):           
        if equal(self.x,other.x) and equal(self.y,other.y):
            return True
        else:
            return False
    def __sub__(self,other): #x-yのベクトルをつくる
        return vector(self.x-other.x, self.y-other.y) 
    def __abs__(self):
        return abs(self.vector)
    def __str__(self):
        return "{:.10f} {:.10f}".format(self.x,self.y)
    
    def dis(self,q,L=2):  #pとqの距離
        if L==2:
            return ((self.x-q.x)**2+(self.y-q.y)**2)**0.5

################################################################   
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vec=complex(x,y)

def dot(v1,v2): #内積
    return (v1.vec*((v2.vec).conjugate())).real

def cross(v1,v2): #外積
    return v1.x*v2.y-v1.y*v2.x
################################################################


def iSP(p,p1,p2):
    """
    3点p,p1,p2の位置関係を返す
    0:p,p1,p2の位置に被りがある
    1:pからみて, p1を反時計回りに回すとp2になる（p→p1→p2と進んだとき, 左に折れて進む）
    2:pからみて, p1を時計回りに回すとp2になる（p→p1→p2と進んだとき, 右に折れて進む）
    3:pからみて, p1とp2が同一直線で反対側にある
    4:pからみて, p1とp2が同一直線で同じ側にある
    ----------
    p: point
        見るときの中心となる点。
    p1,p2: point:

        点
    """

    if p1==p or p2==p or p1==p2:
        return 0
    v1=p1-p
    v2=p2-p
    v1_cross_v2=cross(v1,v2)
    if equal(v1_cross_v2,0):
        v1_dot_v2=dot(v1,v2)
        if v1_dot_v2<0:
            return 3
        else:
            return 4
    else:
        if v1_cross_v2>0:
            return 1
        else:
            return 2

##################################################### 

class Line:  #直線であって線分ではない
    def __init__(self,p,q):
        self.p=p
        self.q=q
        self.dirvec=p-q

def is_parallel(l1,l2):
    if equal(cross(l1.dirvec,l2.dirvec),0):
        return True
    else:
        return False

def is_orthogonal(l1,l2):
    if equal(dot(l1.dirvec,l2.dirvec),0):
        return True
    else:
        return False

def intersect(l1,l2):
    if equal(cross(l1.dirvec,l2.dirvec),0):
        return point(10**20,10**20)
    else:
        vec2=l2.p-l1.p
        t=cross(vec2,-l2.dirvec)/cross(l1.dirvec,-l2.dirvec)
        intpoint=l1.p+l1.dirvec.scmal(t)
        return intpoint


#######################################################
    

class segment:
    def __init__(self,p,q):
        self.start=p
        self.end=q
    
    def dx(self): #x方向の幅
        return self.start.x-self.end.x


######################################################
    

class polygon:
    def __init__(self,lis):
        self.n=len(lis) #リストは適当に並び変えてある前提
        self.lis=lis
    
    def calc_area(self):
        ret=0
        p0=point(0,0)
        for i in range(self.n):
            p1=self.lis[i]
            p2=self.lis[(i+1)%self.n]
            v1=p1-p0
            v2=p2-p0


            ret+=cross(v1,v2)/2
            #print(v1.x,v1.y,v2.x,v2.y,cross(v1,v2)//2)
        return ret
    

N=int(input())
P=[point(*map(int,input().split())) for i in range(N)]

PL=polygon(P)
print('{:.1f}'.format(PL.calc_area()))


