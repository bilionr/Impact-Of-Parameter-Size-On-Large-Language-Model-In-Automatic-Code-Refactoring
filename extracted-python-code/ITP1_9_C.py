n = int(input())
points = [0, 0]
for i in range(n):
    cards = input().split()
    if cards[1] < cards[0]:
        points[0] += 3
    elif cards[0] < cards[1]:
        points[1] += 3
    else:
        points[0] += 1
        points[1] += 1
print(*points)
