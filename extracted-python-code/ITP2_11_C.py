n = input()
lx = list(map(int, input().split()[1:]))

for v in range(1 << len(lx)):
    sum_ = 0
    s = ''
    for i in range(len(format(v, 'b'))):
        if (v >> i) & 1:
            sum_ |= 1 << lx[i]
            s += f" {lx[i]}"
    print(f"{sum_}:{s}")

