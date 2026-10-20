import bisect

d = dict()
keys = []
changed = False
for _ in range(int(input())):
    query = input().split()
    if query[0] == "0":
        if not query[1] in d:
            keys.append(query[1])
            d[query[1]] = [query[2]]
            changed = True
        else:
            d[query[1]].append(query[2])
    elif query[0] == "1":
        if query[1] in d:
            for v in d[query[1]]:
                print(v)
    elif query[0] == "2":
        if query[1] in d:
            d[query[1]] = []
    elif len(d) > 0:
        if changed:
            keys.sort()
            changed = False
        for k in keys[bisect.bisect_left(keys, query[1]):bisect.bisect(keys, query[2])]:
            for v in d[k]:
                print(k, v)
