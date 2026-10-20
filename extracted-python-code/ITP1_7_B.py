while 1:
    ans = 0
    n,x = map(int,input().split())
    if n == 0:
        break
    for i in range(min(n,x-3),x//3,-1):
        y = x-i
        for j in range(min(i-1,y-1),y//2,-1):
            ans += 1
    print(ans)
