import math

def main():
    n = int(input())
    p = list(map(float, input().split()))
    q = list(map(float, input().split()))
    expect_cost = solve_optimal_cost(n, p, q)
    print(f'{expect_cost:.08f}')

# 最適二分探索木の1回の探索コストの期待値を求める
def solve_optimal_cost(n, p, q):
    # opt_e[i][j], opt_ki[i][j]: 探索範囲[i,j]の最適二分探索木の探索コストの期待値、根のインデックスを保持
    opt_e = [[0]*(n+1) for _ in range(n+1)]
    opt_ki = [[-1]*(n+1) for _ in range(n+1)]
    
    ## 方針: p,qにおいて探索範囲[si,ei]を広げながら、各探索範囲における最適な根のインデックスを探す
    ## 探索範囲[si,ei]の部分木は、pはsi~(ei-1)までの要素、qはsi~eiまでの要素で構成される
    # 1. p,qはソート済のため、先に累積確率を求めておく
    # 累積確率: q->p->q の順で与えられた確率を足す
    sum_prb = [0]*(2*(n+1))
    # i//2 は、奇数iの場合、その前の偶数の位置
    for i in range(2*n + 1):
        sum_prb[i+1] = sum_prb[i] + (q[i//2] if i%2 == 0 else p[i//2])

    # 2. 根のみの部分木の探索コストの期待値・根のインデックスを求める（一番小さな部分問題）
    # si = eiの時、この部分木を構成する要素はq[i]のみのため、根のみの部分木となる
    # 根のみのため深さの考慮は不要で、確率がそのまま期待値を表す
    for i in range(n+1):
        opt_e[i][i] = q[i]
        opt_ki[i][i] = i
        
    # 3. 探索範囲を1,2,...,nと広げ、各範囲での部分木の最適な根のインデックス・左右木の探索コストを求める
    for length in range(1, n+1):
        for si in range(n-length+1):
            ei = si + length
            # opt_lrには、探索範囲[si,ei]の左右木の探索コストの期待値が入る
            opt_lr, opt_ki[si][ei] = solve_subtree_optimal(si, ei, opt_e, opt_ki)

            # opt_lrは部分問題のため、探索範囲[si,ei]の全体の最適二分探索木の探索コストの期待値opt_seを加える
            # opt_seは、範囲[si,ei]に含まれる全要素の確率の合計に相当
            # sum_prbは累積確率のため、範囲[si,ei]に含まれる全要素の確率の合計は
            # (ei-1)番目までのp, ei番目までのqの累積確率 － 0~(si-1)番目までのp,qの累積確率
            ## 例えば、範囲[1,2]で考えた時、範囲内の要素はpの1番目、qの1,2番目
            ## (0->)q->p->q->p->q から 最初のq->p->を引くということ
            ## sum_prb[0]は0なので、実際に累積確率が入っているのはsum_prb[1]以降
            opt_se = sum_prb[2*ei+1] - sum_prb[2*si]
            opt_e[si][ei] = opt_lr + opt_se

    return opt_e[0][n]

# 探索範囲[si,ei]の部分木における最適な根のインデックス・左右木の探索コストを求める
def solve_subtree_optimal(si, ei, opt_e, opt_ki):
    # 範囲[si,ei]の部分木の最適な根のインデックスをrとすると、
    # 範囲[si,(ei-1)]の最適二分探索木の根srは、r以下
    # ∵範囲[si,(ei-1)]は、範囲[si,ei]の部分問題であるためその最適な根srは必ず、より大きな問題の最適な根rより大きくならない
    # 同様に範囲[si,ei]は、範囲[(si+1),ei]の部分問題であるため、範囲[(si+1),ei]の最適な根er >= r と言える

    # 範囲[si,ei]の部分木について、rを基準に分割して解く
    # rが取り得る範囲（ループの終端のためerは+1）
    sr = opt_ki[si][ei-1]
    er = min(opt_ki[si+1][ei]+1, ei)
    opt_er = math.inf
    opt_r = si
    for r in range(sr, er):
        expect_cost = opt_e[si][r] + opt_e[r+1][ei]
        if expect_cost < opt_er:
            opt_er = expect_cost
            opt_r = r
    return opt_er, opt_r


if __name__ == '__main__':
    main()
