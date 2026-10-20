visited = []
stack = []

def DFS_visit(s, adj):
    global visited, stack
    
    for v in adj[s]:
        if not visited[v]:
            visited[v] = True
            DFS_visit(v, adj)
    stack.append(s)

def topological_sort(V, adj):
    global visited, stack
    
    visited = [False]*V
    for s in range(V):
        if not visited[s]:
            visited[s] = True
            DFS_visit(s, adj)
    stack.reverse()
    return stack

def convert_to_list_input(user_input):
    input_list = user_input.splitlines()
    v, e = map(int, input_list[0].split())
    data_dict = {i: [] for i in range(v)}

    for line in input_list[1:]:
        if line == "":
            break
        parts = line.split()
        key = int(parts[0])
        values = int(parts[1])
        data_dict[key].append(values)

    return v, data_dict

import sys
user_input = sys.stdin.read()
vertex, item = convert_to_list_input(user_input)
stack = topological_sort(vertex, item)
for i in stack:
    print(i)
