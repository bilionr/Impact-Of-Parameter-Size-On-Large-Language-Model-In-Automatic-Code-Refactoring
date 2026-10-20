import sys

# READ_FROM_FILE = True
READ_FROM_FILE = False


def cross_product(v0, v1):
    return v0.real * v1.imag - v0.imag * v1.real


def is_ccw(p0, p1, p2):
    v01 = p1 - p0
    v12 = p2 - p1
    return cross_product(v01, v12) >= 0


# p_list will be converted.
def calc_convex_hull(n, p_list):
    p_list.sort(key=lambda x: (x.imag, x.real))
    pch_list = []
    for p in p_list:
        while len(pch_list) >= 2 and not is_ccw(pch_list[-2], pch_list[-1], p):
            pch_list.pop()
        pch_list.append(p)

    t = len(pch_list)
    for p in reversed(p_list[:n - 1]):
        while len(pch_list) > t and not is_ccw(pch_list[-2], pch_list[-1], p):
            pch_list.pop()
        pch_list.append(p)
    pch_list.pop()

    return pch_list


def main():
    if READ_FROM_FILE:
        f = open('test0.txt', 'r')
    else:
        f = sys.stdin

    n = int(f.readline())
    p_list = []
    for _ in range(n):
        x, y = map(int, f.readline().split())
        p_list.append(complex(x, y))
    p_ch = calc_convex_hull(n, p_list)

    print(len(p_ch))
    [print(int(p.real), int(p.imag)) for p in p_ch]

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == '__main__':
    main()

