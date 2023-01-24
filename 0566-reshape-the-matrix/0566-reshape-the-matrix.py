class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = [[0 for column in range(c)] for row in range(r)]
        print(ans)
        array = []
        row_size = len(mat)
        col_size = len(mat[0])
        for row in range(row_size):
            for col in range(col_size):
                array.append(mat[row][col])
        for item in range(r):
            for col_item in range(c):
                if len(array) != (r*c):
                    return mat
                else:
                    ans[item][col_item] = array[(item*c)+(col_item)]
        return ans
            
        
                
        