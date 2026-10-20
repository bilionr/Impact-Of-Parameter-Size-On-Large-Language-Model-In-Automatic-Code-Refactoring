# ANm=list(map(int,input().split()))
# ans=False
# for i in range(0,101):
#     tmp=copy.copy(ANm)
#     tmp.append(i)
#     tmp=sorted(tmp)
#     tmp.pop(0)
#     tmp.pop()
#     if sum(tmp)>=X:
#         ans=True
#         break

    
# if ans==True:
#     print(i)
# else:
#     print(-1)

# ans=[]
# for i in range(2,1<<10):
#     x=0
#     for j in range(9,-1,-1):
#         if (i&(1<<j)):
#             x=x*10
#             x+=j
#     ans.append(x)
# print(ans[2])

q=int(input())
query=[list(map(int,input().split())) for _ in range(q)]
S=set()
for i in query:
    q=i[0]
    if q==0:
        S.add(i[1])
        print(len(S))
    elif q==1:
        if i[1] in S:
            print(1)
        else:
            print(0)
    elif q==2:
        S.discard(i[1])
    elif q==3:
        L=i[1]
        R=i[2]
        if len(S) <R-L:
            for x in sorted(S):
                if L <= x <= R:
                    print(x)
                    
        else:
            for i in range(L,R+1):
                if i in S:
                    print(i)

