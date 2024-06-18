class Solution:
    # Function to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # If lengths are different, they cannot be anagrams
        if len(a) != len(b):
            return False
            
        a_count = {}
        b_count = {}
        
        for char in a:
            a_count[char] = a_count.get(char, 0) + 1
            
        for char in b:
            b_count[char] = b_count.get(char, 0) + 1
        
        return a_count == b_count

# Example usage
sol = Solution()
a = "listen"
b = "silent"
print(sol.isAnagram(a, b))  # Output: True

# Additional test cases
a = "b"
b = "d"
print(sol.isAnagram(a, b))  # Output: False
