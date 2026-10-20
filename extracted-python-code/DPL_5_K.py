# ボールと箱11


def main():

    N,K = map(int, input().split())

    mod = 10**9 + 7

    if N > K:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()


