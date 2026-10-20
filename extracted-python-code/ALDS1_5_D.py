def m(x, n):
    global c
    if n <= 64:
        y = [x.pop()]
        for i in x[::-1]:
            n = 0
            for j in y:
                if i < j: break
                n += 1
            c += n
            y.insert(n, i)
        return y
    l = n // 2
    y = m(x[l:], n - l)
    x = m(x[:l], l)
    n = 0
    for j in y:
        while n < l and x[n] < j: n += 1
        c += l - n
    return sorted(x + y)

n = int(input())
c = 0
m([int(s) for s in input().split()], n)
print(c)
