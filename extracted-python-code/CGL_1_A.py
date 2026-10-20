def inner_product(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2

x1, y1, x2, y2 = map(int, input().split())
q = int(input())
v12_x = x2 - x1
v12_y = y2 - y1
for i in range(q):
    x0, y0 = map(int, input().split())
    v10_x = x0 - x1
    v10_y = y0 - y1
    k = inner_product(v10_x, v10_y, v12_x, v12_y) / inner_product(v12_x, v12_y, v12_x, v12_y)
    x = x1 + k * v12_x
    y = y1 + k * v12_y
    print(x, y)
