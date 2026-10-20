n = int(input())

diceref = list(map(int, input().split()))
dicebox = [diceref]

for dn in range(n-1):
    dicesamp = list(map(int, input().split()))
    if diceref[0] and diceref[5] in [dicesamp[0], dicesamp[1], dicesamp[5], dicesamp[4]]:
        for i in range(4):
            if dicesamp[0] == diceref[0] and dicesamp[5] == diceref[5]:
                break
            else:
                dicesamp = [dicesamp[1], dicesamp[5], dicesamp[2], dicesamp[3], dicesamp[0], dicesamp[4]]
        if dicesamp[0] != diceref[0] or dicesamp[5] != diceref[5]:
            dicesamphld = [dicesamp[2], dicesamp[1], dicesamp[5], dicesamp[0], dicesamp[4], dicesamp[3]]
            if dicesamphld[0] == diceref[0] and dicesamphld[5] == diceref[5]:
                dicesamp = dicesamphld
            else:
                dicesamp = [dicesamp[3], dicesamp[1], dicesamp[0], dicesamp[5], dicesamp[4], dicesamp[2]]
    elif diceref[0] in [dicesamp[2], dicesamp[3]]:
        if dicesamp[2] == diceref[0]:
            dicesamp = [dicesamp[2], dicesamp[1], dicesamp[5], dicesamp[0], dicesamp[4], dicesamp[3]]
        else:
            dicesamp = [dicesamp[3], dicesamp[1], dicesamp[0], dicesamp[5], dicesamp[4], dicesamp[2]]

    for j in range(3):
        if dicesamp[1] == diceref[1]:
            break
        else:
            dicesamp = [dicesamp[0], dicesamp[2], dicesamp[4], dicesamp[1], dicesamp[3], dicesamp[5]]
            
    dicebox.append(dicesamp)

count = 0    
for k in range(n-1):
    for l in range(1, n):
        if k < l:
            if dicebox[k] == dicebox[l]:
                count += 1

if count == 0:
    print("Yes")
else:
    print("No")
