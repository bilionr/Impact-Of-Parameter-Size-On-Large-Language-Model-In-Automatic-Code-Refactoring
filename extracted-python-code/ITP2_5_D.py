def solve():
    from itertools import permutations
    n = int(input())
    nums = (str(i) for i in range(1, n + 1))
    ans = (' '.join(t) for t in permutations(nums))
    print('\n'.join(ans))

solve()
