from collections import deque

def bfs(graph, start):
    n = len(graph)
    distances = [-1] * n
    distances[start - 1] = 0
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()
        for neighbor in graph[current_vertex - 1]:
            if distances[neighbor - 1] == -1:
                distances[neighbor - 1] = distances[current_vertex - 1] + 1
                queue.append(neighbor)

    return distances

# Read input
n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    data = input().split()
    u = int(data[0])
    k = int(data[1])
    v = [int(x) for x in data[2:]]
    graph[u - 1] = v

# Perform BFS starting from vertex 1
distances = bfs(graph, 1)  # Start from vertex 1

# Print the results
for vertex_id, distance in enumerate(distances):
    print(f"{vertex_id + 1} {distance}")

