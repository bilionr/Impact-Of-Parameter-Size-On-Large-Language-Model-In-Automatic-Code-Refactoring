from collections import deque
def solve(N, W, items):
    dp = [[0]*(W+1) for _ in range(N+1)]
    
    for i in range(N):
        v, w, m = items[i]
        
        # 各余りについて処理
        for r in range(w):
            # 値の配列を作成
            k_max = (W-r) // w
            deq = deque()  # スライド最大値用のdeque
            
            # 初期値を計算
            for k in range(k_max + 1):
                # dp[i-1][w*k + r] + k*v を計算
                value = dp[i][w*k + r] - k*v
                
                # dequeの末尾から、今の値より小さい値を削除
                while deq and deq[-1][1] <= value:
                    deq.pop()
                
                # 新しい値を追加
                deq.append((k, value))
                
                # スライド窓の範囲外の値を削除
                if deq[0][0] <= k - m - 1:
                    deq.popleft()
                
                # 最大値を設定
                dp[i+1][w*k + r] = deq[0][1] + k*v
    return max(dp[-1])
                
N,W = map(int,input().split())
items = [[int(x) for x in input().split()] for _ in range(N)]
print(solve(N,W,items))
