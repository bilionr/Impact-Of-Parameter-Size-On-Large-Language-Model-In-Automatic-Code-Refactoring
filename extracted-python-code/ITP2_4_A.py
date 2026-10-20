n = int(input())
a = list(map(int,input().split()))
q = int(input())
for i in range(q):
    b,e = map(int,input().split())
    a[b:e] = reversed(a[b:e])
print(" ".join(map(str,a)))
