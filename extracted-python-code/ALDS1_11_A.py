def main():
    n = int(input())
    adj = [[0]*n for _ in range(n)] # adj[row][column]
    for _ in range(n):
        table = list(map(int, input().split()))
        row = table[0]-1
        num = table[1]
        if num == 0:
            continue
        for i in range(2, num+2):
            column = table[i]-1
            adj[row][column] = 1
    for i in range(n):
        print(*adj[i])

if __name__ == '__main__':
    main()
