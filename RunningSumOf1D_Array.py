"""
Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0] ...nums[i]).
Example:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""
#Constraints:
#The number of nodes in the list is in range [1,1000].
#The value of each element in the array is in the range [-10^6, 10^6].

def Solution(num):
    results = [0] * len(num)
    results[0] = num[0]
    for i in range(0, len(num)):
        results[i] = num[i] + results[i-1]
    return results
        


num=[3,1,2,10,1]
print(Solution(num))
    
    