b = int(input())

for a in range(1, b+1):
    if a % 3 == 0 or a % 10 == 3 or "3" in str(a):
        print(" " + str(a), end="")
