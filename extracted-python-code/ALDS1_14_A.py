T=input()
P=input()
for i in range(len(T)):
    if i+len(P)>len(T):
        break
    if P==T[i:i+len(P)]:
        print(i)
        
    
