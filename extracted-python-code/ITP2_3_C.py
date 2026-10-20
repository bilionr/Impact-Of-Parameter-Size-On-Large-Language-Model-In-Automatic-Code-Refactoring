n = int(input())
nums = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    b, e, k = map(int,input().split())
    print((nums[b:e]).count(k))

