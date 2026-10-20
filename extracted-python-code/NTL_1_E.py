# ext euc
import io
import sys
import bisect
import math
from itertools import permutations, combinations
from heapq import heappush, heappop
from collections import deque
from collections import defaultdict as dd
sys.setrecursionlimit(10**7+10)

mod = 998244353

_INPUT = """\
3 8
"""

def ext_euc(a, b):
    """
    ax + by = 1の解を求める
    """
    if b==0:
        return (1, 0)
    else:
        xd, yd = ext_euc(b, a%b)
        return (yd, xd - a//b * yd)

def main():
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    a//=g
    b//=g
    print(*ext_euc(a, b))
    
if __name__ == "__main__":
    # sys.stdin = io.StringIO(_INPUT)
    main()
