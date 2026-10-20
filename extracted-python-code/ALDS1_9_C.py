#きついのでheapqライブラリ関数使う
import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    
    #イテレータに変換
    iterator = iter(input_data)
    
    Q = []
    
    #出力結果を溜めておくリスト
    results = []
    
    for command in iterator:
        if command == 'insert':
            key = int(next(iterator))
            
            heapq.heappush(Q, -key)
            
        elif command == 'extract':
            if Q:

                max_val = -heapq.heappop(Q)
                results.append(str(max_val))
                
        elif command == 'end':
            break
    print('\n'.join(results))

if __name__ == "__main__":
    main()
