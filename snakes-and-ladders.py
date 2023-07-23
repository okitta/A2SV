class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        for i in range(1,len(board),2): board[i].reverse()
        linearBoard = [0] + list(chain(*board))

        
        queue, seen, curToken, cnt = [1], set(), 1, 0
        seen.add(curToken)
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                print(cur,cnt)
                if cur == len(linearBoard) -1: return cnt

                for i in range(cur+1, min(cur+7,len(linearBoard))):
                    nxt = linearBoard[i] if linearBoard[i] != -1 else i

                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
            cnt += 1
        return -1