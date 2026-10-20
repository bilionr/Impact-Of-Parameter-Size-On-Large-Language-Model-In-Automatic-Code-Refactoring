import bisect

d = dict()
keys = []
changed = False
for _ in range(int(input())):
    query = input().split()
    if query[0] == "0":
        if not query[1] in d:
            keys.append(query[1])
            changed = True
        d[query[1]] = query[2]
    elif query[0] == "1":
        print(d[query[1]] if query[1] in d else 0)
    elif query[0] == "2":
        d[query[1]] = "0"
    elif len(d) > 0:
        if changed:
            keys.sort()
            changed = False
        for k in keys[bisect.bisect_left(keys, query[1]):bisect.bisect(keys, query[2])]:
            if not d[k] == "0":
                print(k, d[k])
