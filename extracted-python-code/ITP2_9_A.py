import sys

def main():
    input = sys.stdin.readline

    n = int(input())
    A = list(map(int, input().split()))
    
    m = int(input())
    B = list(map(int, input().split()))
    
    i = j = 0
    union = []
    while i < n and j < m:
        if A[i] < B[j]:
            union.append(A[i]); i += 1
        elif A[i] > B[j]:
            union.append(B[j]); j += 1
        else:
            union.append(A[i]); i += 1; j += 1
    while i < n:
        union.append(A[i]); i += 1
    while j < m:
        union.append(B[j]); j += 1

    sys.stdout.write('\n'.join(map(str, union)) + '\n')

if __name__ == "__main__":
    main()

