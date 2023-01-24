class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column_size = len(matrix[0])
        row_size = len(matrix)
        for row in range(row_size):
            row_min = min(matrix[row])
            row_max = max(matrix[row])
            if target < row_min or target > row_max:
                pass
            else:
                for column in range(column_size):
                    if matrix[row][column] == target:
                        return True
        return False
        