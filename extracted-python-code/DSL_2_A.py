from sys import stdin, stdout


class SegmentTree:
    def __init__(self, n):
        self.N = 1
        while self.N < n:
            self.N *= 2
        self.INF = 2 ** 31 - 1
        self.tree = [self.INF] * (2 * self.N)

    def update(self, i, x):
        i += self.N
        self.tree[i] = x
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2 * i] if self.tree[2 * i] < self.tree[2 * i + 1] else self.tree[2 * i + 1]

    def find(self, l, r):
        l += self.N
        r += self.N
        result = self.INF
        while l <= r:
            if l % 2 == 1:
                result = result if result < self.tree[l] else self.tree[l]
                l += 1
            if r % 2 == 0:
                result = result if result < self.tree[r] else self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return result


def main():
    read = stdin.readline
    write = stdout.write

    n, q = map(int, read().split())
    seg = SegmentTree(n)

    answer = []
    for _ in range(q):
        com, x, y = map(int, read().split())
        if com == 0:
            seg.update(x, y)
        else:
            l, r = (x, y) if x < y else (y, x)
            answer.append(seg.find(l, r))
    write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()

