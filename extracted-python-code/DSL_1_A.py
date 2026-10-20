class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    
    ds = DisjointSet(n)
    
    index = 2
    result = []
    
    for _ in range(q):
        com = int(data[index])
        x = int(data[index + 1])
        y = int(data[index + 2])
        index += 3
        
        if com == 0:
            ds.unite(x, y)
        elif com == 1:
            if ds.same(x, y):
                result.append("1")
            else:
                result.append("0")
    
    print("\n".join(result))

if __name__ == "__main__":
    main()

