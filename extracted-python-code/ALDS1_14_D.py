from bisect import bisect_left


def main():
    t = input()
    n = len(t)
    s = [t[i:i + 1000] for i in range(n)]
    s.sort()
    q = int(input())
    for _ in range(q):
        p = input()
        pos = bisect_left(s, p)
        print(1 if pos < n and p in s[pos] else 0)


if __name__ == '__main__':
    main()

