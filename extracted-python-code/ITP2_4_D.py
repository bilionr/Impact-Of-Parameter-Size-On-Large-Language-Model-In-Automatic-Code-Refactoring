n = int(input())
A = list(input().split())
ans = []

bef = ""
for a in A:
  if a != bef:
    bef = a
    ans.append(a)

print(" ".join(ans))
