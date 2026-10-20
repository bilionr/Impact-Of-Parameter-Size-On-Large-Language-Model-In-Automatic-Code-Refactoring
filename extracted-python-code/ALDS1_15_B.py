def fractional_knapsack(N, W, items):
    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    for value, weight in items:
        if W == 0:
            break
        # Take as much as we can from the current item
        amount = min(weight, W)
        total_value += amount * (value / weight)
        W -= amount
    
    return total_value

# Input handling
N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

# Output the maximum total value
print(f"{fractional_knapsack(N, W, items):.6f}")

