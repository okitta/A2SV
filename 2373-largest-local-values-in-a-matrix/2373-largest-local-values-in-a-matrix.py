class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row_size = len(grid)
        col_size = len(grid[0])
        result = [[0 for col in range(col_size-2)] for row in range(row_size-2)]
        ans = []
        max_array = []
        for row in range(row_size-2):
            for col in range(col_size-2):
                ans.append([grid[i][col:col+3] for i in range(row,row+3)])
        for item in range(len(ans)):
            find_max = 0
            for item1 in range(len(ans[0])):
                if find_max < max(ans[item][item1]):
                    find_max = max(ans[item][item1])
            max_array.append(find_max)
        for item in range(row_size-2):
            for col_item in range(col_size-2):
                    result[item][col_item] = max_array[(item*(col_size-2))+(col_item)]
        return result
                    
                
        