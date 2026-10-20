N = 8

rs = []
cs = []
k = int(input())
for i in range(k):
    r, c = map(int, input().split())
    rs.append(r)
    cs.append(c)


def put(col):
    for i in range(k):
        if col[rs[i]] != cs[i]:
            return
    for i in range(N):
        for j in range(N):
            if col[i] == j:
                print('Q', end='')
            else:
                print('.', end='')
            if j == N-1:
                print()


def check(x, col):
    for i, row in enumerate(reversed(col), 1):
        if (x + i == row) or (x - i == row):
            return False
    return True


def search(col):
    if len(col) == N:
        put(col)
        return
    for i in range(N):
        if i in col:
            continue
        if check(i, col) == True:
            col.append(i)
            search(col)
            col.pop()


search([])

