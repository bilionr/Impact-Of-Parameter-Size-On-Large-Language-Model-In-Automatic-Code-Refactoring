Lst=list(map(str,input().split(', ')))
for i in range(len(Lst)):
    temp=''
    for j in range(len(Lst[i])):
        for k in Lst[i][j]:
            if k.islower():
                temp+=k.upper()
            elif k.isupper():
                temp+=k.lower()
            else:
                temp+=k
    Lst[i]=temp
print(', '.join(Lst))
