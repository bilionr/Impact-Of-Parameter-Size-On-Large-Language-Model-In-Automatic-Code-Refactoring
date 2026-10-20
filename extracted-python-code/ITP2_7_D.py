def lower_bound(target, array, start, end) -> int:
    if end-start == 1:
        return start if array[start] >= target else end
    mid = (start+end)//2
    if array[mid] < target:
        return lower_bound(target, array, mid, end)
    else:
        return lower_bound(target, array, start, mid)

s = set()
d = dict()
count = 0
for _ in range(int(input())):
    query = [int(x) for x in input().split()]
    if query[0] == 0:
        if not query[1] in s:
            d.update({query[1]:1})
            s.add(query[1])
        else:
            d[query[1]] += 1
        count += 1
        print(count)
    elif query[0] == 1:
        print(d[query[1]] if query[1] in s else 0)
    elif query[0] == 3 and len(s) > 0:
        if len(s) < query[2]-query[1]:
            l = list(s)
            l.sort()
            for i in range(lower_bound(query[1], l, 0, len(l)), len(l)):
                if l[i] <= query[2]:
                    for _ in range(d[l[i]]):
                        print(l[i])
                    continue
                break
        else:
            for i in range(query[1], query[2]+1):
                if i in s:
                    for _ in range(d[i]):
                        print(i)
    elif query[1] in s:
        c = d[query[1]]
        s.remove(query[1])
        d.pop(query[1])
        count -= c
