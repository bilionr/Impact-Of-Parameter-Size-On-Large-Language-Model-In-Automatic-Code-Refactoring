from sys import stdin, stdout

OPERATIONS = ["test", "set", "clear", "flip", "all", "any", "none", "count", "val"]
BIT_LENGTH = 64


def main():
    lines = stdin.readlines()
    write = stdout.write

    n = int(lines[0])
    masks = []
    for line in lines[1:n + 1]:
        k, *args = map(int, line.split())
        mask = 0
        for b in args:
            mask += 2 ** b
        masks.append(mask)

    # q = int(lines[0])
    flags = 0

    for line in lines[n + 2:]:
        query, *args = map(int, line.split())

        if OPERATIONS[query] == "test":
            i = args[0]
            write(f'{1 if flags & 1 << i else 0}\n')

        elif OPERATIONS[query] == "set":
            m = args[0]
            flags |= masks[m]

        elif OPERATIONS[query] == "clear":
            m = args[0]
            flags &= (2 ** BIT_LENGTH - 1) - masks[m]

        elif OPERATIONS[query] == "flip":
            m = args[0]
            flags ^= masks[m]

        elif OPERATIONS[query] == "all":
            m = args[0]
            write(f'{1 if masks[m] == (flags & masks[m]) else 0}\n')

        elif OPERATIONS[query] == "any":
            m = args[0]
            write(f'{1 if flags & masks[m] else 0}\n')

        elif OPERATIONS[query] == "none":
            m = args[0]
            write(f'{1 if not (flags & masks[m]) else 0}\n')

        elif OPERATIONS[query] == "count":
            m = args[0]
            write(f'{f"{(flags & masks[m]):b}".count("1")}\n')

        elif OPERATIONS[query] == "val":
            m = args[0]
            write(f'{(flags & masks[m])}\n')


main()

