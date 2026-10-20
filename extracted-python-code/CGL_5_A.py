import sys
import math
import operator

# READ_FROM_FILE = True
READ_FROM_FILE = False


def calc_closest_dist(point_list):
    n = len(point_list)
    if n <= 1:
        return math.inf

    mid = n // 2
    x = point_list[mid][0]
    d = min(calc_closest_dist(point_list[:mid]), calc_closest_dist(point_list[mid:]))

    point_list.sort(key=operator.itemgetter(1))

    py_list = []
    for p in point_list:
        if abs(p[0] - x) >= d:
            continue
        for py in reversed(py_list):
            dx = abs(py[0] - p[0])
            dy = abs(py[1] - p[1])

            if dy >= d:
                break
            d = min(d, math.sqrt(dx**2 + dy**2))

        py_list.append(p)

    return d


def main():
    if READ_FROM_FILE:
        f = open('test0.txt', 'r')
    else:
        f = sys.stdin

    n = int(f.readline())

    point_list = [tuple(map(float, f.readline().split())) for _ in range(n)]
    point_list.sort()
    min_dist = calc_closest_dist(point_list)
    print(f'{min_dist:.6f}')

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == '__main__':
    main()

