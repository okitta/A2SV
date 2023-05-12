class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1])])
        steps = 0
        while q:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()
                if r < 0 or r == m or c < 0 or c == n or maze[r][c] == '+':
                    continue
                if (r == m - 1 or c == n - 1 or r == 0 or c == 0) and steps:
                    return steps
                maze[r][c] = '+'
                q.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])
            steps += 1
        return -1