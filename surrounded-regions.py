class Solution:
    """ Do not return anything, modify board in-place instead. """
    
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and board[row][col] == 'O'
        
        def dfs(row, col):
            seen.add((row, col))
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    dfs(new_row, new_col)

        for row in range(m):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][-1] == 'O':
                dfs(row, n - 1)
        for col in range(n):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[-1][col] == 'O':
                dfs(m - 1, col)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O' and (i, j) not in seen:
                    board[i][j] = 'X'
        return