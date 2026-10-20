# コインの組み合わせ 2
# 解けなかった
# 半分全列挙


# # WA 解法
# from itertools import combinations
# import bisect

# def main():

#     N,K,L,R = map(int, input().split())

#     A = list(map(int, input().split()))

#     a_l = A[:N//2]
#     a_r = A[N//2:]

#     a_l_tot = []
#     a_r_tot = []

#     for i in combinations(a_l,K//2):
#         a_l_tot.append(sum(i))
#     a_l_tot.sort()

#     for i in combinations(a_r, K-(K//2)):
#         a_r_tot.append(sum(i))
#     a_r_tot.sort()

#     ans = 0
#     for i in a_l_tot:
#         LL = L-i
#         RR = R-i
#         l_index = bisect.bisect_left(a_r_tot, LL)
#         r_index = bisect.bisect_right(a_r_tot, RR)

#         ans += r_index - l_index
    
#     print(ans)


# if __name__ == '__main__':
#     main()


# 解答例

def main():
    from itertools import combinations
    from bisect import bisect_left as bl
    from bisect import bisect_right as br


    # 入力
    N, K, L, R = map(int, input().split())
    a = list(map(int, input().split()))


    # P[k] == a の前半の要素を丁度 k 個使った和のリスト(ソートもしておく)
    # Q[k] == a の後半の要素を丁度 k 個使った和のリスト(ソートもしておく)
    P = [sorted([sum(c) for c in combinations(a[:N // 2], k)]) for k in range(K + 1)]
    Q = [sorted([sum(c) for c in combinations(a[N // 2:], k)]) for k in range(K + 1)]


    # 答えの計算
    ans = 0
    for k in range(K + 1):

        # 前半を k 個 後半を K - k 個使う
        p, q = P[k], Q[K - k]
        for s in p:
        
            # q の要素 t で L - s 以上 R - s 以下となるものの数を足す
            # つまり L <= s + t <= R を満たす t の数
            ans += br(q, R - s) - bl(q, L - s)

    
    # 出力
    print(ans)


if __name__ == '__main__':
    main()


