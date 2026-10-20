def f(vwm,W):
    if W<=0: return 0
    if len(vwm)==0: return 0
    vw,v,w,m = vwm[0]
    Ans = 0
    if w*m<=W:
        Ans = max(Ans,v*m + f(vwm[1:],W-w*m))
        Ans = max(Ans,v*(m-1) + f(vwm[1:],W-w*(m-1)))
        if m>2: Ans = max(Ans,v*(m-2) + f(vwm[1:],W-w*(m-2)))
    else:
        Ans = max(Ans,v*(W//w) + f(vwm[1:],W-w*(W//w)))
        if W//w>0: Ans = max(Ans,v*((W//w)-1) + f(vwm[1:],W-w*((W//w)-1)))
        if W//w>1: Ans = max(Ans,v*((W//w)-2) + f(vwm[1:],W-w*((W//w)-2)))
    return Ans

N,W = map(int,input().split())
vwm = []
for _ in range(N):
    v,w,m = (map(int,input().split()))
    vwm.append([v/w,v,w,m])
vwm = sorted(vwm,reverse=True)
Ans = f(vwm,W)
print(Ans)
