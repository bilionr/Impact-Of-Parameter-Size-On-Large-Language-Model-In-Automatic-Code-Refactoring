def solve():
    from sys import stdin
    
    f_i = stdin
    N, Q = map(int, f_i.readline().split())
    
    a = tuple(map(int, f_i.readline().split()))
    
    answers = []
    init_ans = N * (N - 1) // 2 + N
    for x_i in map(int, f_i.readline().split()):
        ans = init_ans
        total = 0
        l = 0
        for a_i in a:
            total += a_i
            while x_i < total:
                total -= a[l]
                l += 1
            ans -= l
        answers.append(ans)
    
    print(*answers, sep='\n')

solve()
