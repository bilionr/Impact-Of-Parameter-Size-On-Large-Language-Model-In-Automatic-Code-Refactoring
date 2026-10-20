n=int(input())
L=list(map(int, input().split()))
max=min=sum=L[0]
for i in range(1,n):
    sum+=L[i]
    if L[i]>max:
        max=L[i]
    if L[i]<min:
        min=L[i]
print(min,max,sum)    
