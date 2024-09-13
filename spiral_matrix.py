def spiral_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    ans = []
    i, j = 0, 0
    RIGHT, LEFT, DOWN, TOP = 0, 1, 2, 3
    direction = RIGHT
    TOP_WALL = 0
    RIGHT_WALL = n
    LEFT_WALL = -1
    DOWN_WALL = m
    
    while len(ans) != m*n:
        if direction == RIGHT:
            while j < RIGHT_WALL:
                ans.append(matrix[i][j])
                j += 1
            i, j = i+1, j-1
            RIGHT_WALL -= 1
            direction = DOWN
        elif direction == DOWN:
            while i < DOWN_WALL:
                ans.append(matrix[i][j])
                i += 1
            i, j = i-1, j-1
            DOWN_WALL -= 1
            direction = LEFT
        elif direction == LEFT:
            while j > LEFT_WALL:
                ans.append(matrix[i][j])
                j -= 1
            i, j = i-1, j+1
            LEFT_WALL += 1
            direction = TOP
        else:
            while i > TOP_WALL:
                ans.append(matrix[i][j])
                i -= 1
            i, j = i+1, j+1
            TOP_WALL += 1
            direction = RIGHT
    return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
print(spiral_matrix(matrix))

#Time Complexity: O(m*n)