def find_symmetric_difference(A, B):
    """
    Find symmetric difference of sets A and B 
    (elements in either A or B, but not both)
    Time complexity: O(n+m)
    Space complexity: O(n+m)
    """
    # Initialize pointers and result list
    i, j = 0, 0
    symmetric_diff = []
    
    # Traverse both arrays
    while i < len(A) and j < len(B):
        # If elements are equal, skip both
        if A[i] == B[j]:
            i += 1
            j += 1
        # If A's element is smaller, add to symmetric difference
        elif A[i] < B[j]:
            symmetric_diff.append(A[i])
            i += 1
        # If B's element is smaller, add to symmetric difference
        else:
            symmetric_diff.append(B[j])
            j += 1
    
    # Add remaining elements from A, if any
    while i < len(A):
        symmetric_diff.append(A[i])
        i += 1
    
    # Add remaining elements from B, if any
    while j < len(B):
        symmetric_diff.append(B[j])
        j += 1
    
    return symmetric_diff

def solve():
    # Read size of first set
    n = int(input())
    # Read first set
    A = list(map(int, input().split()))
    
    # Read size of second set
    m = int(input())
    # Read second set
    B = list(map(int, input().split()))
    
    # Compute symmetric difference
    symmetric_diff_result = find_symmetric_difference(A, B)
    
    # Print result
    for num in symmetric_diff_result:
        print(num)

# Run the solution
if __name__ == "__main__":
    solve()
