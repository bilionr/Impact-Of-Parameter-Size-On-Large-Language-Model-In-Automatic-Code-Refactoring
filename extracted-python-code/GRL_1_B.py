from enum import Enum
import sys
sys.setrecursionlimit(10**6)

hasinf = False
inf = 1234567890

def goldberg_radzik(G, s, V):
  global hasinf
  class State(Enum):
    UNREACHED = 0
    LABELED = 1
    SCANNED = 2
  
  d = {}
  parent = {}
  for v in range(V):
    d[v] = inf

  d[s] = 0

  B = {s}
  iter = 0
  while len(B) > 0:
    iter +=1
    
    A = set()
    del_list = []
    for v in B:
      updated = False
      for w in G[v]:
        cost = G[v][w]
        if cost + d[v] < d[w]: # admissible
          d[w] = cost + d[v]
          parent[w] = v
          A.add(w)
          updated = True
      if not updated:
        del_list.append(v)

    # topo sort
    neg_loop_start = None
    def dfs(v, visited, topo_list):
      nonlocal neg_loop_start

      if v in visited:
        if visited[v] == 1:
          return False
      else:
        visited[v] = 1
        for w in G[v]:
          cost = G[v][w]
          if cost + d[v] < d[w]: # admissible
            parent[w] = v
            d[w] = cost + d[v]
            if not dfs(w, visited, topo_list):
              if neg_loop_start is None:
                neg_loop_start = v
              return False
        visited[v] = 0
        topo_list.append(v)
      return True

    visited = {}
    topo_list = []
    is_dag = True
    for v in A:
      if not v in visited:
        is_dag = is_dag and dfs(v, visited, topo_list)

    if not is_dag:
      hasinf = True
      return {}
    topo_list.reverse()

    # scan
    B = set()
    for v in topo_list:
      for w in G[v]:
        cost = G[v][w]
        if d[v] + cost < d[w]: # admissible
          parent[w] = v
          d[w] = d[v] + cost
          B.add(w)

    if iter > 20:
      raise
  return d

n, m, s = [int(x) for x in input().split()]
G = [{} for _ in range(n)]
for i in range(m):
  a, b, c = [int(x) for x in input().split()]
  G[a][b] = c

d = goldberg_radzik(G, s, n)
if hasinf:
  print('NEGATIVE CYCLE')
else:
  for i in range(n):
    print(d[i] if d[i] != inf else 'INF')

