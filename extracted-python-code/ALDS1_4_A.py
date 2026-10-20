n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))
obs = 0

for i in T:
    if i in S:
        obs += 1

print(obs)
