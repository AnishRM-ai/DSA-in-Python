"""Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, find the maximum element in the array.
Note: If the array is increasing then just print the last element will be the maximum value.

Example 1:

Input: 
n = 9
arr[] = {1,15,25,45,42,21,17,12,11}
Output: 45
Explanation: Maximum element is 45.
"""
class Solution:

    def findMaximum(self, arr, n):
        if n == 1:
            return arr[0]
        
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if mid is the peak element
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
                return arr[mid]
            
            # If the middle element is greater than the left neighbor and less than the right neighbor
            elif mid < n - 1 and arr[mid] < arr[mid + 1]:
                left = mid + 1
            
            # If the middle element is greater than the right neighbor and less than the left neighbor
            else:
                right = mid - 1
        
        # This line should never be reached if the input conditions are guaranteed (array strictly increases then maybe strictly decreases)
        return -1

# Example usage:
n = 9
arr = [1, 15, 25, 45, 42, 21, 17, 12, 11]
sol = Solution()
print(sol.findMaximum(arr, n))  # Output: 45
