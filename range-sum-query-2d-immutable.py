class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        rows,cols = len(matrix),len(matrix[0])
        hor_pref = [[0]*(cols+1) for _ in range(rows+1)]
        for row in range(rows):
            for col in range(cols):
                hor_pref[row+1][col+1] = hor_pref[row+1][col]+hor_pref[row][col+1] - hor_pref[row][col]+matrix[row][col]
                

        self.matrix = hor_pref
            
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        answer = self.matrix[row2][col2]-self.matrix[row1-1][col2]-self.matrix[row2][col1-1]+self.matrix[row1-1][col1-1]
        return answer
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)