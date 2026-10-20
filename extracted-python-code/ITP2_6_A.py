import sys
import bisect

def main():
    input = sys.stdin.readline
    
    n = int(input())
    A = list(map(int, input().split()))
    
    q = int(input())
    out = []
    
    for _ in range(q):
        k = int(input())
        i = bisect.bisect_left(A, k)
        if i < n and A[i] == k:
            out.append('1')
        else:
            out.append('0')
    
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
    main()

