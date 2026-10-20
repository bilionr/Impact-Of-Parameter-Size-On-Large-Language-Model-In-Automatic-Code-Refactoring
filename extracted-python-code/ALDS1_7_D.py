def reconstruct(l, r):
  global preorder, inorder, ans
  if l >= r:
    return 
  root = preorder.pop(0)
  center = inorder.index(root)

  reconstruct(l, center)
  reconstruct(center+1, r)
  ans.append(root)
  
N = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))
ans = []

reconstruct(0, N)
print(*ans)

