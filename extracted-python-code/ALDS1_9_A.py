N = int(input())
L = list(map(int,input().split()))


for n in range(1,N+1):
    print('node ' + str(n) + (':'), end = ' ')
    key = L[n-1]
    print('key = ' + str(key),end = ', ' )
    if n > 1:
        parent = int(n/2)
        parentkey = L[parent - 1]
        print('parent key = ' + str(parentkey), end = ', ')
        
    if n*2 <= N:
        leftkey = L[n*2 - 1]
        print('left key = ' + str(leftkey), end = ', ')
        
        if n*2 + 1 <= N:
            rightkey = L[n*2]
            print('right key = ' + str(rightkey), end = ', ')
            
    print()
