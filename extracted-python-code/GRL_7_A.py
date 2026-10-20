import sys
input = sys.stdin.buffer.readline
from collections import defaultdict as dd,deque

##二部マッチング
##参考:https://snuke.hatenablog.com/entry/2019/05/07/013609


class Bipartile_Matching:

    def __init__(self,L,R):


        ##L2R:Lから見たRのマッチングを記録
        ##R2L:Rから見たLのマッチングを記録
        ##backpath:L側に逆辺が張られている場合の辿る先
        ##root:逆辺を考慮したLの始点を記録

        self.L=L
        self.R=R
        self.L2R=[-1]*L
        self.R2L=[-1]*R
        self.backpath=[-1]*L
        self.root=[-1]*L
        self.edge=dd(list)

    def add_edge(self,s,t):
        self.edge[s].append(t)


    def match(self):
        res=0
        f=True
        while f:
            f=False
            q=deque()
            for i in range(L):
                ##まだマッチング対象が見つかっていなければ
                ##iを始点としてキューに追加
                if self.L2R[i]==-1:
                    self.root[i]=i
                    q.append(i)

            while q:
                s=q.popleft()

                ##逆辺を辿った先のrootが-1になっていればcontinue
                if ~self.L2R[self.root[s]]: continue
                
                ##始点から接続されている辺を全探索する
                for t in self.edge[s]:

                    if self.R2L[t]==-1:
                        ##逆辺が存在する場合は辿っていく
                        while t!=-1:
                            self.R2L[t]=s
                            self.L2R[s],t=t,self.L2R[s]
                            s=self.backpath[s]

                        f=True
                        res+=1
                        break

                    ##仮のtに対するマッチング候補の情報を更新しキューに追加する
                    temps=self.R2L[t]
                    if ~self.backpath[temps]:continue

                    self.backpath[temps]=s
                    self.root[temps]=self.root[s]
                    q.append(temps)


            ##更新があれば逆辺・始点情報を初期化する
            if f:
                self.backpath=[-1]*L
                self.root=[-1]*L

        return res


L,R,E=map(int,input().split())

G=Bipartile_Matching(L,R)
for i in range(E):
    a,b=map(int,input().split())
    G.add_edge(a,b)
    

res=G.match()
print(res)
