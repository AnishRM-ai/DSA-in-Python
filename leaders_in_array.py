def leaders(A, N):
        # This will hold the leaders in the array
        leaders = []
        
        # Start with the rightmost element, which is always a leader
        max_from_right = A[-1]
        leaders.append(max_from_right)
        
        # Traverse the array from the second last element to the first element
        for i in range(N-2, -1, -1):
            if A[i] >= max_from_right:
                leaders.append(A[i])
                max_from_right = A[i]
        
        # The leaders are collected in reverse order, reverse the list before returning
        leaders.reverse()
        return leaders

# Example usage:
A = [16, 17, 4, 3, 5, 2]
N = len(A)
print(leaders(A, len(A))) 