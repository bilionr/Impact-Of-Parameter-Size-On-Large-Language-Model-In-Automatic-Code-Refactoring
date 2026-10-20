n = int(input())
al = list(map(int, input().split()))
m = int(input())
bl = list(map(int, input().split()))

ans = sorted(set(al) - set(bl))
if ans:
    print(*ans, sep="\n")

