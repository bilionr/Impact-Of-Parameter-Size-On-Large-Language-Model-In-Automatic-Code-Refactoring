l=list(map(int,input().split()))
j=0
for i in range(l[1]-l[0]+1):
    if l[2]%(l[0]+i)==0:
        j=j+1
    else:
        j=j

print(j)
