#Function to find equilibrium point in the array.
def equilibriumPoint(A, N):
        # Your code here
        total_array = sum(A)
        left_sum = 0
        
        for i in range(len(A)):
            # Update right sum by subtracting the current element
            total_array -= A[i]
            if left_sum == total_array: #check if the left sum is equal to right sumn
                return i + 1
            
            left_sum += A[i] # update left sum for next iteration.
        
        return -1
            
arr = [1, 3, 5, 2, 2]
n = 5
print(equilibriumPoint(arr, n)) 