def allPairs(A, B, N, M, X):
    # Create a set for elements in B
    B_set = set(B)
    
    # List to store the pairs
    result = []
    
    # Find all pairs (A[i], B[j]) such that A[i] + B[j] == X
    for a in A:
        complement = X - a
        if complement in B_set:
            result.append((a, complement))
    
    # Sort the result list by the first element of the pairs
    result.sort()
    
    return result

# Example usage
A = [1, 2, 3, 4, 5]
B = [5, 6, 7, 8, 9]
N = len(A)
M = len(B)
X = 10

pairs = allPairs(A, B, N, M, X)
print(pairs)  # Output: [(1, 9), (2, 8), (3, 7), (4, 6)]
