# aizu_ITP2_6_B_Includes.py

n = int(input())
A = set(list(map(int,input().split())))

m = int(input())
B = set(list(map(int,input().split())))

print( int(B <= A))
