def partition(A, p, r):
    x = A[r][1] 
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def is_stable(original, sorted_cards):
    # dict: number -> list of suits (入力順)
    from collections import defaultdict
    orig_order = defaultdict(list)
    for suit, num in original:
        orig_order[num].append(suit)
    for suit, num in sorted_cards:
        if orig_order[num][0] != suit:
            return False
        orig_order[num].pop(0)
    return True

def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    cards = [input().strip().split() for _ in range(n)]
    cards = [(suit, int(num)) for suit, num in cards]
    
    original = cards[:]
    
    quicksort(cards, 0, n - 1)

    print("Stable" if is_stable(original, cards) else "Not stable")
    for suit, num in cards:
        print(f"{suit} {num}")

if __name__ == "__main__":
    main()

