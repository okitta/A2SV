class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        mrow, mcol = len(grid), len(grid[0]) # dimension 
        
        def fn(iterator, iterator1):
            seen = set()
            row, col = [0]*3, [0]*3 # row sum & column sum 
            diag = anti = 0
            for index1 in range(iterator-1, iterator+2):
                for index2 in range(iterator1-1, iterator1+2):
                    if not 0 <= grid[index1][index2] < 10 or grid[index1][index2] in seen: 
                        return False 
                    seen.add(grid[index1][index2])
                    row[index1-iterator+1] += grid[index1][index2]
                    col[index2-iterator1+1] += grid[index1][index2]
                    if index1-index2 == iterator-iterator1: diag += grid[index1][index2]
                    if index1+index2 == iterator+iterator1: anti += grid[index1][index2]
            return len(set(row)) == 1 and len(set(col)) == 1 and row[0] == col[0] == diag == anti
        
        ans = 0
        for iterator in range(1, mrow-1):
            for iterator1 in range(1, mcol-1): 
                if grid[iterator][iterator1] == 5 and fn(iterator, iterator1): 
                    ans += 1
        return ans 