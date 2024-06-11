"""
    Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

If there are multiple solutions, find the lexicographically smallest one.

Note:The given array is sorted in ascending order, and you don't need to return anything to make changes in the original array itself.
    """
    
from typing import List

class Solution:
    def convertToWave(self, n: int, a: List[int]) -> None:
        # Traverse all even indexed elements
        for i in range(0, n-1, 2):
            # Swap if current even index element is smaller than next
            a[i], a[i+1] = a[i+1], a[i]


arr = [1, 2, 3, 4, 5, 6]
solution = Solution()
solution.convertToWave(len(arr), arr)
print(arr)  
