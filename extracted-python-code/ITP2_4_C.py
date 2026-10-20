input()
*a,=map(int,input().split())
for i in range(int(input())):
    l,r,t=map(int,input().split())
    a[l:r],a[t:t+r-l]=a[t:t+r-l],a[l:r]
print(*a)
