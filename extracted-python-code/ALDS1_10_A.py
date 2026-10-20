la = [1, 1]

n = int(input())
while len(la) <= n:
    la.append(la[-1] + la[-2])

print(la[n])

