import sys

lines = sys.stdin.readlines()

# n = int(lines[0])
l = []
for line in lines[1:]:
    lx = line.split()
    l.append(tuple((int(lx[0]), int(lx[1]), lx[2], int(lx[3]), lx[4])))
for item in sorted(l):
    print(*item)
