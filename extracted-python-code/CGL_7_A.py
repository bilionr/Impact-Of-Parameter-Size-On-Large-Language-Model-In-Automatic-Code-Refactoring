def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def main(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)
    if d + r1 == r2 or d + r2 == r1:
        return 1
    if d <= r1 - r2 or d <= r2 - r1:
        return 0
    elif d < r1 + r2:
        return 2
    elif d == r1 + r2:
        return 3
    else:
        return 4
        
if __name__ == '__main__':
    # args
    arg1 = [int(x) for x in input().split(" ")]
    arg2 = [int(x) for x in input().split(" ")]
    inputs = arg1 + arg2
    print(main(*inputs))

