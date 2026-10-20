n = int(input())
L = list(map(int,input().split()))


def turn(L,i,n): #長さnのリストLのi番とそれ以降を逆向きにする
    for k in range((n-i)//2):
        L[i+k],L[n-1-k] = L[n-1-k],L[i+k]
    return L

L_1 = L.copy()
i = n-1
while i > 0:
    if L[i] < L[i-1]:
        L.append(n+1)
        j = i
        while L[i-1] > L[j]:
            j += 1
        del L[n]
        L_1[i-1],L_1[j-1] = L_1[j-1],L_1[i-1]
        
        L_1 = turn(L_1,i,n)
        print(' '.join(list(map(str,L_1))))
        break
    i -= 1
    
        
print(' '.join(list(map(str,L))))


L_2 = L.copy()
i = n-1

while i > 0:
    if L[i] > L[i-1]:
        L.append(0)
        j = i
        while L[i-1] < L[j]:
            j += 1
        del L[n]
        L_2[i-1],L_2[j-1] = L_2[j-1],L_2[i-1]
        
        L_2 = turn(L_2,i,n)
        print(' '.join(list(map(str,L_2))))
        break
    i -= 1
    
        

        
    
 
    
        
        

