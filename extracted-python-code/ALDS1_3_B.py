from collections import deque
import sys

def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    
    # プロセスキューを作成（名前, 残り時間）
    queue = deque()
    for _ in range(n):
        name, time = input().split()
        queue.append((name, int(time)))

    total_time = 0  # 経過時間
    result = []

    while queue:
        name, time = queue.popleft()
        if time <= q:
            total_time += time
            result.append(f"{name} {total_time}")
        else:
            total_time += q
            queue.append((name, time - q))

    # 出力
    print("\n".join(result))

if __name__ == "__main__":
    main()
