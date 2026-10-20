# ボールと箱 4

import math


def main():

    N,K = map(int, input().split())
    mod = 10**9 + 7

    ans = math.factorial(N+K-1) // (math.factorial(N)*math.factorial(K-1))
    print(ans % mod)

if __name__ == '__main__':
    main()





