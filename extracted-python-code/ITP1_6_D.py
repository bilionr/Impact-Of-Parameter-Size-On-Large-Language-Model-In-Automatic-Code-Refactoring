n,m=map(int,input().split())
A=[[0 for i in range(m)] for j in range(n)]
print
for i in range(n):
    A[i]=list(map(int,input().split()))
B=[0 for i in range(m)]
for i in range(m):
    B[i]=int(input())
C=[0 for i in range(n)]
for i in range(n):
    for j in range(m):
        C[i]+=A[i][j]*B[j]
    print(C[i])
