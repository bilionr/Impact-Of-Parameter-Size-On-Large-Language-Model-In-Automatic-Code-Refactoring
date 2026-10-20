def solve(x, y):
    pm = [0 for _ in range(ord('z') - ord('A') + 1)]
    for i, c in enumerate(x):
        pm[c] += 1 << i

    V = (1 << len(x)) - 1

    for c in y:
        V = ((V + (V & pm[c])) | (V & ~pm[c]))

    ans = bin(V)[-len(x):].count("0")

    return ans


if __name__ == "__main__":
    q = int(input())

    for _ in range(q):
        x = tuple(ord(c) - ord('A') for c in input())
        y = tuple(ord(c) - ord('A') for c in input())
        print(solve(x, y))

