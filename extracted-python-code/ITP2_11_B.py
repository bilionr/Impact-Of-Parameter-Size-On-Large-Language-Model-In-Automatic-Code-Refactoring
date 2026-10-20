from sys import stdin, stdout


def main():
    write = stdout.write

    n = int(stdin.readline())
    k, *b = map(int, stdin.readline().split())
    b = set(b)

    for i in range(2 ** n):
        bits = []
        for j in range(n):
            if 1 & i >> j:
                bits.append(j)
        if b.issubset(bits):
            if bits:
                write(f'{i}: {" ".join(map(str, bits))}\n')
            else:
                write(f'{i}:\n')


main()
