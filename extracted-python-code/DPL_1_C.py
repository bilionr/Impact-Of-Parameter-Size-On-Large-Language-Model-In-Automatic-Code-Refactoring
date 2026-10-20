n, c = map(int, input().split())
goods = [tuple(map(int, input().split())) for _ in range(n)]
goods.sort(key=lambda x: x[0] / x[1], reverse=True)
items = []
item_check = set()
for v, w in goods:
    if w in item_check:
        continue
    item_check.update(set(range(w, c + 1, w)))
    items.append((v, w))

dp_table = [0] * (c + 1)
for v, w in items:
    for j in range(w, c + 1):
        if dp_table[j] < dp_table[j - w] + v:
            dp_table[j] = dp_table[j - w] + v
print(dp_table[-1])

