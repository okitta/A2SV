class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_size = len(grid)
        check_col = [[0 for index in range(grid_size)] for index in range(grid_size)]
        counter = 0
        # check_size = len(check_col)
        for col in range(len(grid)):
            for row in range(len(grid)):
                check_col[col][row] = grid[row][col]
        
        for index in range(grid_size):
            for item in range(grid_size):
                if grid[index] == check_col[item]:
                    counter += 1
        return counter
            
        