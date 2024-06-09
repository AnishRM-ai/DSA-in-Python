def search(arr, N, X):
    index = -1  # Initialize the index to -1, assuming X is not found
    for i in range(N):
        if arr[i] == X:
            index = i
            break
    return index, N

# Example usage
arr = [1, 2, 3, 4, 5]
N = len(arr)
X = 3

index, total_indices = search(arr, N, X)
print(f"Index: {index}, Number of indices: {total_indices}")  # Output: Index: 2, Number of indices: 5

X = 6
index, total_indices = search(arr, N, X)
print(f"Index: {index}, Number of indices: {total_indices}")  # Output: Index: -1, Number of indices: 5
