# The Maximum Number of Customers

import sys

input = sys.stdin.readline

def main():

    N,T = map(int, input().split())
    times = [0]*(T+1)

    for i in range(N):
        l,r = map(int, input().split())
        times[l] += 1
        times[r] -= 1
    
    for i in range(1,T+1):
        times[i] += times[i-1]
    
    ans = 0

    for i in range(T+1):
        ans = max(ans, times[i])
    
    print(ans)
    


if __name__ == '__main__':
    main()


