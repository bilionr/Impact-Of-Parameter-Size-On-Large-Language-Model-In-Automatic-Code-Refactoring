def min_coins(n):
    coins = [25, 10, 5, 1]  # コインの種類
    total_coins = 0  # 必要なコインの数
    for coin in coins:
        total_coins += n // coin  # 各コインで作成できるお釣りの数
        n %= coin  # 残りのお釣り
    return total_coins

n = int(input().strip())
print(min_coins(n))
