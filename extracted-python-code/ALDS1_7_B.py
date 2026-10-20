class Node:
  def __init__(self, chs, pa=-1):
    self.chs = chs
    self.pa = pa

n = int(input())
tree = {id:Node(chs=[-1,-1]) for id in range(-1, n)}
for _ in range(n):
  id, *chs = map(int, input().split())
  tree[id].chs = chs
  for ch in chs:
    tree[ch].pa = id

def set_d_and_h(id, d):
  tree[id].d = d
  h = 0
  for ch in tree[id].chs:
    if ch != -1:
      h = max(h, set_d_and_h(ch, d+1) + 1)
  tree[id].h = h
  return h

for id in tree:
  if tree[id].pa == -1:
    set_d_and_h(id, 0)
    break

for id, node in tree.items():
  if id != -1:
    sib = tree[node.pa].chs[1] if tree[node.pa].chs[0] == id else tree[node.pa].chs[0]
    deg = 2 - node.chs.count(-1)  
    kind = "root" if node.pa == -1 else "internal node" if deg else "leaf"
    print(f"node {id}: parent = {node.pa}, sibling = {sib}, degree = {deg}, depth = {node.d}, height = {node.h}, {kind}")

