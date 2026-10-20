import itertools
n,k=map(int,input().split())
def generate(n,k):
    l=[i for i in range(n)]
    m=list(itertools.combinations(l,k))
    ans=[]
    for x in m:
        an=0
        for j in x:
            an|=1<<j
        ans.append((an,*sorted(x)))
    return ans
a=generate(n,k)
a=sorted(a)
for i in range(len(a)):
    b,*c=a[i]
    print(f"{a[i][0]}: {' '.join(map(str,a[i][1:]))}")
