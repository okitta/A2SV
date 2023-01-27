class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_row = set()
        set_col = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    set_row.add(row)
                    set_col.add(col)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in set_row or col in set_col:
                    matrix[row][col] = 0
        print(matrix)
            
            
                