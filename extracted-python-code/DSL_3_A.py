def find_smallest_subarray(N, S, arr):
    # Initialize variables
    left = 0  # Left pointer of the window
    current_sum = 0  # Sum of current window
    min_length = float('inf')  # Minimum window length

    # Iterate through the array with right pointer
    for right in range(N):
        # Expand the window by adding current element
        current_sum += arr[right]

        # Shrink the window from left while sum is greater than or equal to S
        while current_sum >= S:
            # Update minimum length
            min_length = min(min_length, right - left + 1)
            
            # Remove leftmost element and move left pointer
            current_sum -= arr[left]
            left += 1

    # Return 0 if no subarray found, else return minimum length
    return min_length if min_length != float('inf') else 0

# Read input
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Find and print the smallest subarray length
print(find_smallest_subarray(N, S, arr))
