"""
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.
"""
from collections import deque

class Solution:
    
    # Function to find the maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):
        if n * k == 0:
            return []

        if k == 1:
            return arr

        deq = deque()
        result = []

        for i in range(n):
            # Remove elements out of this window from the front of the deque
            if deq and deq[0] == i - k:
                deq.popleft()

            # Remove elements that are smaller than the current element from the back of the deque
            while deq and arr[deq[-1]] < arr[i]:
                deq.pop()

            deq.append(i)

            # Starting from index k-1, append the maximum element of each subarray to the result
            if i >= k - 1:
                result.append(arr[deq[0]])

        return result

# Example usage:
solution = Solution()
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(solution.max_of_subarrays(arr, len(arr), k))  # Output: [3, 3, 5, 5, 6, 7]
