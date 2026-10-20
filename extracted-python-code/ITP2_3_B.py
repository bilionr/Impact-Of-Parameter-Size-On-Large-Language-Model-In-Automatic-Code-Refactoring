n = int(input())
a = list(map(int,input().split()))
q = int(input())
for i in range(q):
    m,b,c = map(int,input().split())
    if m == 0:
        print(min(a[b:c]))
    else:
        print(max(a[b:c]))
