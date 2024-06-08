class Solution:
    def longestCommonPrefix(self, arr, n):
        if n == 0:
            return -1
        
        # Initialize the prefix as the first string
        prefix = arr[0]
        
        for i in range(1, n):
            # Check the common prefix between the current prefix and the next string
            while arr[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return -1
        
        return prefix if prefix else -1

# Example usage
solution = Solution()
strings = ["flower", "flow", "flight"]
n = len(strings)
print(solution.longestCommonPrefix(strings, n))  # Output: "fl"

# Case with no common prefix
strings = ["dog", "racecar", "car"]
n = len(strings)
print(solution.longestCommonPrefix(strings, n))  # Output: -1
