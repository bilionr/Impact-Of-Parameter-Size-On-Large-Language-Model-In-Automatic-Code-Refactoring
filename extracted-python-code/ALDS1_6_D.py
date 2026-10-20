input()
a = [int(s) for s in input().split()]
l = min(a)
a = dict(list(zip(sorted(a), a))[::-1])
c = 0

while a:
    m, n = a.popitem()
    k = 0
    while m != n:
        c += n
        n = a.pop(n)
        k += 1
    c += min(m * k, 2 * (m + l) + l * k)

print(c)
