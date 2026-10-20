import itertools
n=int(input())
mx=1001
tbl=[[0]*mx for _ in range(mx)]
for _ in range(n):
    x1,y1,x2,y2=map(int,input().split())
    tbl[x1][y1]+=1
    tbl[x1][y2]-=1
    tbl[x2][y1]-=1
    tbl[x2][y2]+=1
ay=[list(itertools.accumulate(t)) for t in tbl]
ax=[]
for x in zip(*ay):
    ax.append(list(itertools.accumulate(x)))
ans=0
for x in ax:
    ans=max(ans,max(x))
print(ans)
