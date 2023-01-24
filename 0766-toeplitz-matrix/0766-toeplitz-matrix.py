class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dictionary = {}
        column_size = len(matrix[0])
        row_size = len(matrix)
        for row in range(row_size):
            for column in range(column_size):
                if (row - column) in dictionary:
                    if matrix[row][column] == dictionary[row-column]:
                        pass
                    else:
                        return False
                else:
                    dictionary[row-column] = matrix[row][column]
        return True
        