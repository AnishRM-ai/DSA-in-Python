"""
Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.

Example 1:

Input:
N = 3, sum = 4
coins = {1,2,3}
Output: 4
Explanation: Four Possible ways are: {1,1,1,1},{1,1,2},{2,2},{1,3}.

"""

def countWaysToMakeSum(N, sum, coins):
    dp = [0] * (sum + 1)
    dp[0] = 1  # Base case: one way to make sum 0
    
    for coin in coins:
        for i in range(coin, sum + 1):
            dp[i] += dp[i - coin]
    
    return dp[sum]

# Example usage
N = 3
sum_value = 4
coins = [1, 2, 3]
print(countWaysToMakeSum(N, sum_value, coins))  # Output: 4
