# ヒストグラムの中の最大長方形

import sys

input = sys.stdin.readline


def main():

    N = int(input())
    H_list = list(map(int, input().split()))
    H_list.append(0)
    ans = 0
    stack = []
    for i,v in enumerate(H_list):
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
                ans = max(ans, (i-i_left)*h)
            stack.append((i_left,v))
    
    print(ans)


if __name__ == '__main__':
    main()


