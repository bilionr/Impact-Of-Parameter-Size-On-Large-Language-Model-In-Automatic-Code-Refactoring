read = input().split()

a = int(read[0])
b = int(read[1])
c = int(read[2])

first = min(a, b, c)
third = max(a, b, c)
middle = a + b + c - first - third

print(first, middle, third)
