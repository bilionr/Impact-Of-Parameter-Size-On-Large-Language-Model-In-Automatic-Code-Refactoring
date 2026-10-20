# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_B

N = int(input())
S = set(map(int, input().split()))
q = int(input())
T = set(map(int, input().split()))

common_elements = S & T
ans = len(common_elements)
print(ans)
