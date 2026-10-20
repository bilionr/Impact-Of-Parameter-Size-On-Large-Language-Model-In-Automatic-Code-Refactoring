def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # Initialize a 64-bit state with all flags OFF (0)
    state = 0
    results = []

    # Read number of queries
    q = int(data[0])

    # Process each query
    for i in range(1, q + 1):
        query = data[i].split()
        operation = int(query[0])

        if operation == 0:  # test(i)
            index = int(query[1])
            results.append((state >> index) & 1)

        elif operation == 1:  # set(i)
            index = int(query[1])
            state |= (1 << index)

        elif operation == 2:  # clear(i)
            index = int(query[1])
            state &= ~(1 << index)

        elif operation == 3:  # flip(i)
            index = int(query[1])
            state ^= (1 << index)

        elif operation == 4:  # all
            results.append(1 if state == (1 << 64) - 1 else 0)

        elif operation == 5:  # any
            results.append(1 if state != 0 else 0)

        elif operation == 6:  # none
            results.append(1 if state == 0 else 0)

        elif operation == 7:  # count
            results.append(bin(state).count('1'))

        elif operation == 8:  # val
            results.append(state)

    # Print all results for test, all, any, none, count, and val operations
    sys.stdout.write("\n".join(map(str, results)) + "\n")


solve()
