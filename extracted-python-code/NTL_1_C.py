from math import lcm

n = int(input())
A = list(map(int, input().split()))

print(lcm(*A))
