class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        color_pre = image[sr][sc]
        def inbound(row,col):
            return (0 <= row < len(image)) and (0 <= col < len(image[0]))
        def dfs(row,col): 
            image[row][col] = color
            for row_change,col_change in direction:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row,new_col) and image[new_row][new_col] == color_pre:

                    dfs(new_row,new_col)
        if image[sr][sc] != color:
            dfs(sr,sc)
        return image