def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    k = int(data[1])
    weights = list(map(int, data[2:2+n]))

    def can_carry(x):
        if x < max(weights):
            return False
        
        track = 0
        cnt = 0
        for weight in weights:
            if weight <= track:
                track -= weight
            else:
                cnt += 1
                track = x - weight
        
        return cnt <= k

    ok = sum(weights)
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if can_carry(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

if __name__ == "__main__":
    main()

