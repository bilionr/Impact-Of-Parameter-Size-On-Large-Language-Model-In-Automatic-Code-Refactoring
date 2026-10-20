import sys
input = sys.stdin.readline

class RangeSumSegTree:
	def __init__(self, n):
		self.a = [0] * n
		self.n = n
	def add(self, p, x):
		while p < self.n:
			self.a[p] += x
			p |= p + 1
	def sum(self, l, r):
		ans = 0
		r -= 1
		l -= 1
		while r >= 0:
			ans += self.a[r]
			r = (r & r + 1) - 1
		while l >= 0:
			ans -= self.a[l]
			l = (l & l + 1) - 1
		return ans

n, q = map(int, input().split())
seg = RangeSumSegTree(n)
for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 0:
        seg.add(x - 1, y)
    else:
        print(seg.sum(x - 1, y))
