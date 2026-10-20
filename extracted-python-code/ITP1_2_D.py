read = input().split()

w = int(read[0])
h = int(read[1])
x = int(read[2])
y = int(read[3])
r = int(read[4])

if (x + r) > w or (x - r) < 0 or (y + r) > h or (y - r) < 0:
    print("No")
else:
    print("Yes")
