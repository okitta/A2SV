class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        # click on unrevealed mine
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board


        directions = [[-1, -1], [-1, 0], [-1, 1],  \
                      [ 0, -1],          [ 0, 1],  \
                      [ 1, -1], [ 1, 0], [ 1, 1]]

        visited = set()
        stack   = deque()
        row_n   = len(board)
        col_n   = len(board[0])


        # add click to stack
        stack.append(click)
        while stack:
            r, c = stack.pop()
            
            if (r, c) in visited:   continue
            visited.add((r, c))

            # counting mines in adjacent cells
            cnt = 0
            for r_dlt, c_dlt in directions:
                if 0 <= r + r_dlt < row_n and \
                   0 <= c + c_dlt < col_n:
                    cnt += 1   if board[r + r_dlt][c + c_dlt] == 'M'   else 0

            # modify board array
            if cnt == 0:   board[r][c] = 'B'
            else:          board[r][c] = str(cnt)
                
            if cnt != 0:  continue   # found cell with adjacent mine --> move to the next cell in stack
            
            # found cell without adjacent mine --> add adjacent cells
            for r_dlt,c_dlt in directions:
                if 0 <= r + r_dlt < row_n and \
                   0 <= c + c_dlt < col_n:
                    stack.append([r + r_dlt, c + c_dlt])
        
        return board