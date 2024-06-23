class Solution:
    def insert(self, alist, index, n):
        key = alist[index]
        j = index - 1
        # Move elements of alist[0..index-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < alist[j]:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key

    # Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        # Traverse through 1 to n
        for i in range(1, n):
            # Insert alist[i] into the sorted sequence alist[0..i-1]
            self.insert(alist, i, n)

# Example usage
sol = Solution()
arr = [12, 11, 13, 5, 6]
sol.insertionSort(arr, len(arr))
print("Sorted array is:", arr)
