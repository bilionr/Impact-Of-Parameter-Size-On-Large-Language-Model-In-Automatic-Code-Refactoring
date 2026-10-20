class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(V, edges):
    edges.sort(key=lambda x: x[2]) 
    ds = DisjointSet(V)
    mst_weight = 0
    mst_edges = 0
    
    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_weight += weight
            mst_edges += 1
            if mst_edges == V - 1:
                break
    
    return mst_weight

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    V = int(data[0])
    E = int(data[1])
    
    edges = []
    index = 2
    for _ in range(E):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        edges.append((u, v, w))
        index += 3
    
    result = kruskal(V, edges)
    print(result)

if __name__ == "__main__":
    main()

