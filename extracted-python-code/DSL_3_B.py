import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

input = lambda: sys.stdin.readline().strip()

Max = lambda x, y: x if x > y else y
Min = lambda x, y: x if x < y else y
Inf = 10**19

def main():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    cnt = {i: 0 for i in range(1, k+1)}

    ans = Inf
    l = 0
    found = 0
    for r, x in enumerate(a):
        if x in cnt:
            cnt[x] += 1
            if cnt[x] == 1:
                found += 1
        while found == k:
            ans = min(ans, r - l + 1)
            dv = a[l]
            if dv in cnt:
                cnt[dv] -= 1
                if cnt[dv] == 0:
                    found -= 1
            l += 1
    
    print(ans if ans != Inf else 0)

if __name__ == "__main__":
    main()
