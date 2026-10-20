r,c=map(int,input().split())
A=[[0 for i in range(c+1)] for j in range(r+1)]
for k in range(r):
    A[k]=list(map(int,input().split()))
    temp=0
    for m in range(c):
        temp+=A[k][m]
    A[k].append(temp)
for n in range(c+1):
    temp=0
    for o in range(r+1):
        temp+=A[o][n]
    A[r][n]=temp
for p in range(r+1):
    print(' '.join(map(str,A[p])))    
