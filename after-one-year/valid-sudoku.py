class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    item = board[row][col]

                    # Row check
                    key = f'{item} in row {row}'

                    if key in check:
                        return False
                    else:
                        check.add(key)

                    # Column check
                    key = f'{item} in col {col}'

                    if key in check:
                        return False
                    else:
                        check.add(key)

                    # Box check
                    boxIndex = (row // 3) * 3 + (col // 3)
                    key = f'{item} in box {boxIndex}'

                    if key in check:
                        return False
                    else:
                        check.add(key) 

        return True

        