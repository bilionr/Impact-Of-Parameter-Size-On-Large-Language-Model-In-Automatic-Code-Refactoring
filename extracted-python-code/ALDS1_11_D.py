import sys
def s():
 e=sys.stdin.readline
 n,m=map(int,e().split())
 P=[[]for _ in[0]*n]
 C=[0]*n
 k=0
 for _ in[0]*m:
  s,t=map(int,e().split());P[s]+=[t];P[t]+=[s]
 for i in range(n):
  k+=1
  if C[i]<1:
   s=[i];C[i]=k
   while s:
    u=s.pop()
    for v in P[u]:
     if C[v]<1:C[v]=k;s+=[v]
 for _ in[0]*int(e()):
  a,b=map(int,e().split())
  print(['no','yes'][C[a]==C[b]])
s()

