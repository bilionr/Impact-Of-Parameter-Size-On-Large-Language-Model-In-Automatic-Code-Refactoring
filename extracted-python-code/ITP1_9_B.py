while True:
    deck = input()
    if deck == "-":
        break
    h = 0
    for i in range(int(input())):
        h += int(input())
    h %= len(deck)
    print(deck[h:] + deck[:h])

