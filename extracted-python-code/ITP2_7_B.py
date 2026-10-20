import sys

lines = sys.stdin.readlines()

# q = lines[0]
s = set()
for line in lines[1:]:
    lx = line.split()
    if lx[0] == '0':
        s.add(lx[1])
        print(len(s))
    elif lx[0] == '1':
        print(int(lx[1] in s))
    else:
        if lx[1] in s:
            s.remove(lx[1])
