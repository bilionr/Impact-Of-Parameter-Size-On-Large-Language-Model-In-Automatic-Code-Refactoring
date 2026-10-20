while True:
    H,W=map(int,input().split())
    n=W//2
    r=W%2
    if H==W==0:
        break
    else:
        for h in range(H):
            if h%2==0:
                print("#."*n+"#"*r)
            else:
                print(".#"*n+"."*r)
    print()
    
