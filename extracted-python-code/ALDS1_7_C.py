class Node:
  def __init__(self, no, parent, child):
    self.no    = no
    self.parent = parent
    self.child = child

# 二分木を行きがけ順でなぞる
def preorder(trees, i):
  if i<0:
    return
  print(f" {i}", end="")
  preorder(trees, trees[i].child[0]) # left
  preorder(trees, trees[i].child[1]) # right

# 二分木を通りがけ順でなぞる
def inorder(trees, i):
  if i < 0:
    return
  inorder(trees, trees[i].child[0]) # left
  print(f" {i}", end="")
  inorder(trees, trees[i].child[1]) # right

# 二分木を帰りがけ順でなぞる
def postorder(trees, i):
  if i < 0:
    return
  postorder(trees, trees[i].child[0]) # left
  postorder(trees, trees[i].child[1]) # right
  print(f" {i}", end="")

N = int(input())
trees = [ Node(i, -1, [-1, -1]) for i in range(N) ]
for _ in range(N):
    no, *child = list(map(int, input().split()))
    trees[no].child = child
    # mark parent
    for ch in child:
        if ch>=0:
            trees[ch].parent = no

root  = 0
for i in range(N):
  if trees[i].parent == -1:
    root = i

print("Preorder")
preorder(trees, root)
print()
print("Inorder")
inorder(trees, root)
print()
print("Postorder")
postorder(trees, root)
print()
