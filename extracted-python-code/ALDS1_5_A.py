_ = input()
s = set([0])

for m in [int(s) for s in input().split()]:
    s = s | {n + m for n in s}

_ = input()
for m in [int(s) for s in input().split()]:
    print('yes' if m in s else 'no')
