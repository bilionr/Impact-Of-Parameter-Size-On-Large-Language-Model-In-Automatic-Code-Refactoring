import sys
from collections import deque

def process_queries(n, queries):
    # 各キューを管理するリスト（初期状態は空の deque）
    queues = [deque() for _ in range(n)]
    
    results = []  # front 操作の出力を蓄積（入出力効率向上）

    for query in queries:
        op, t = query[0], query[1]
        
        if op == 0:
            # enqueue(t, x): Q[t] に整数 x を挿入
            queues[t].append(query[2])
        elif op == 1:
            # front(t): Q[t] の先頭要素を出力（空の場合は何もしない）
            if queues[t]:
                results.append(str(queues[t][0]))
        elif op == 2:
            # dequeue(t): Q[t] の先頭要素を削除（空の場合は何もしない）
            if queues[t]:
                queues[t].popleft()

    # 最後にまとめて出力（高速化のため）
    sys.stdout.write("\n".join(results) + "\n")

# 標準入力の読み込み（sys.stdin.read() を使用して高速化）
if __name__ == "__main__":
    input_data = sys.stdin.read().splitlines()
    n, q = map(int, input_data[0].split())
    queries = [list(map(int, line.split())) for line in input_data[1:]]
    process_queries(n, queries)

