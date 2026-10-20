def gcd(a,b):
    while a % b != 0:
        x = b
        b = a % b
        a = x
    return b

x,y = map(int,input().split())
A = gcd(x,y)
print(A)
