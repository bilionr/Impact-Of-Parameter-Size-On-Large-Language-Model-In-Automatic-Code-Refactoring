while True:
    a_0,op,b_0=map(str,input().split())
    a=int(a_0)
    b=int(b_0)
    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op=="*":
        print(a*b)
    elif op=="/":
        print(a//b)
    else:
        break
