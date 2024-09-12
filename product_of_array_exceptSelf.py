"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
def productExceptSelf(nums):
    left_multi = 1
    right_multi = 1
    n = len(nums)
    left_arr = [0]*n
    right_arr = [0]*n
    
    for i in range(n):
        j = -i -1
        left_arr [i] = left_multi
        right_arr[j] = right_multi
        left_multi *= nums[i]
        right_multi *= nums[j]
    
    return [l*r for l, r in zip(left_arr, right_arr)]

arr = [1,2,3,4]
print(productExceptSelf(arr))
arr = [-1,1,0,-3,3]
print(productExceptSelf(arr))