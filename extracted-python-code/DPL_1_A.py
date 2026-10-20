n, m = map(int,input().split())
coins = list(map(int, input().split()))
coins.sort(reverse=True)


def coin_changing(balance, usable_coins, upper_bound):
    if balance == 0:
        return 0
    coin = usable_coins.pop(0)
    if upper_bound > balance:
        upper_bound = balance
    if balance % coin == 0:
        return balance // coin
    if balance // coin >= upper_bound:
        return upper_bound
    for i in range(balance // coin, 0, -1):
        answer = coin_changing(balance - coin * i, usable_coins[:], upper_bound - i)
        if upper_bound > answer + i:
            upper_bound = answer + i
    while usable_coins[0] > balance:
        usable_coins.pop(0)
    answer = coin_changing(balance, usable_coins[:], upper_bound)
    return upper_bound if upper_bound <= answer else answer


print(coin_changing(n, coins[:], n))

