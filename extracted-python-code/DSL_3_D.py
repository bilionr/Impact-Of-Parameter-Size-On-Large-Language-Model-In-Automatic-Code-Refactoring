from typing import Generic, Iterable, TypeVar
from collections import deque
T = TypeVar('T')

class SlidingWindowMinimum(Generic[T]):

  def __init__(self, a: Iterable[T]):
    self.a = list(a)
    self.n = len(self.a)

  def build(self, k: int):
    assert 1 <= k <= self.n
    a, n = self.a, self.n
    dq = deque()
    ans = []
    for i in range(n):
      while dq and a[dq[-1]] > a[i]:
        dq.pop()
      dq.append(i)
      if dq and dq[0] <= i-k:
        dq.popleft()
      if i >= k-1:
        ans.append(a[dq[0]])
    self.ans = ans
    return ans

n, l = map(int, input().split())
A = list(map(int, input().split()))
swm = SlidingWindowMinimum(A)
ans = swm.build(l)
print(*ans)

