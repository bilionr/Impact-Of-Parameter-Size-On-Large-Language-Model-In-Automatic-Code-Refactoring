def online_back(p0, p1, p2):
    return p2[0] < p0[0] < p1[0] or p2[0] > p0[0] > p1[0] or p2[1] < p0[1] < p1[1] or p2[1] > p0[1] > p1[0]


def online_front(p0, p1, p2):
    return p0[0] < p1[0] < p2[0] or p0[0] > p1[0] > p2[0] or p0[1] < p1[1] < p2[1] or p0[1] > p1[1] > p2[1]


def on_segment(p0, p1, p2):
    return p0[0] >= p2[0] >= p1[0] or p0[0] <= p2[0] <= p1[0] or p0[1] >= p2[1] >= p1[1] or p0[1] <= p2[1] <= p1[1]


def cross(p0, p1, p2):
    val = (p1[1] - p0[1]) * (p2[0] - p1[0]) - (p1[0] - p0[0]) * (p2[1] - p1[1])
    if val > 0:
        return 1
    elif val < 0:
        return 0
    else:
        if online_back(p0, p1, p2):
            return 2
        elif online_front(p0, p1, p2):
            return 3
        elif on_segment(p0, p1, p2):
            return 4


def main():
    orientation = ["COUNTER_CLOCKWISE", "CLOCKWISE", "ONLINE_BACK", "ONLINE_FRONT", "ON_SEGMENT"]
    x0, y0, x1, y1 = map(int, input().split())
    q = int(input())
    for _ in range(q):
        x2, y2 = map(int, input().split())
        result = cross((x0, y0), (x1, y1), (x2, y2))
        print(orientation[result])
        

if __name__ == '__main__':
    main()

