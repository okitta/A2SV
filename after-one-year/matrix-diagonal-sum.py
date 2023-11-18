class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = set()
        res = 0
        first_row,first_col,second_row,second_col = 0, 0,0,len(mat)-1
        while first_row < len(mat) and first_col < len(mat):
            if (first_row,first_col) not in visited:
                visited.add((first_row,first_col))
                res += mat[first_row][first_col]
            first_row += 1
            first_col += 1
                
        while second_row < len(mat) and second_col >= 0:
            if (second_row,second_col) not in visited:
                visited.add((second_row,second_col))
                res += mat[second_row][second_col]
            second_row += 1
            second_col -= 1
        # print(visited)
        return res

        