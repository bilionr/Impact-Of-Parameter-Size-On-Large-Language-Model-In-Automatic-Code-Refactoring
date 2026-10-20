import heapq

def main():
    n = int(input())
    G = [[] for _ in range(n)]

    # make adjacency list
    for v in range(n):
        for w, c in enumerate(map(int, input().split())):
            if c != -1:
                G[v].append((w, c))


    # Prim's algorithm
    # the list which check the vertex or not
    marked = [False for _ in range(n)]
    cost = 0
    # at first we need to check the vertex of 0
    marked[0] = True
    # heap
    heap = []

    # save the edge which adjacent to vertex 0
    for j, c in G[0]:
        heapq.heappush(heap, (c, j))

    # roop until we checked every vertex
    while heap:
        c, i = heapq.heappop(heap)
        if marked[i]:
            continue
        # marked the vertex
        marked[i] = True
        cost += c
        # save the edge which adjacent to vertex i
        for j, c in G[i]:
            if marked[j]:
                continue
            heapq.heappush(heap, (c, j))
    print(cost)

if __name__ == '__main__':
    main()
