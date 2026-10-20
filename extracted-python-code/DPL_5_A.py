import sys
input = lambda: sys.stdin.readline().rstrip()
MOD=10**9+7

# ボールをどの箱に入れるかがK通り
# それぞれ組み合わせてN乗

N,K=map(int,input().split())
print(pow(K,N,MOD))
