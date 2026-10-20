while True:
    num=input()
    if num=='0':
        break
    ans=0
    for i in num:
        ans+=int(i)
    print(ans)
