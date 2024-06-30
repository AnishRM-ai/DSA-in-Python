class Solution:
    def transpose(self, matrix, n):
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

# Example usage:
solution = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matrix)
transposed_matrix = solution.transpose(matrix, n)
for row in transposed_matrix:
    print(row)
