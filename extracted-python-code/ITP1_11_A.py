dice = [int(s) for s in input().split()]
cmds = input()
for c in cmds:
    if c == "E":
        w = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = w
    elif c == "W":
        w = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = w
    elif c == "N":
        w = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = w
    else:
        w = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = w
print(dice[0])

