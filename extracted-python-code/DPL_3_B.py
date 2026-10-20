# 最大長方形
# ネットで調べた


import sys
from itertools import product, chain

input = sys.stdin.readline


def main():
    
    H,W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(H)]

    T = []
    pre_tmp = [0]*W
    for c in C:
        tmp = []
        for cc, pre in zip(c, pre_tmp):
            if cc == 1:
                tmp.append(0) 
            else:
                tmp.append(pre+1)
        T.append(tmp)
        pre_tmp = tmp.copy()
    
    ans = 0
    for t in T:
        ans = max(ans, get_largest_rectangle(t))
    
    print(ans)


def get_largest_rectangle(hist: list):
    # ヒストグラムが渡されたときに、その中の最大の長方形を返す

    hist = hist.copy()
    hist.append(0)
    ret = 0
    stack = []
    for i,v in enumerate(hist):
        # vが蟻本で言うrectのこと
        if len(stack) == 0:
            stack.append((i,v))
        elif stack[-1][1] < v:
            stack.append((i,v))
        elif stack[-1][1] > v:
            while stack and stack[-1][1] > v:
                # スタックが空でなく、最後の要素がvより大きい限りは
                # 面積の最大値を更新していく
                i_left, h = stack.pop()
                ret = max(ret, (i-i_left)*h)
            stack.append((i_left,v))
    
    return ret


if __name__ == '__main__':
    main()


