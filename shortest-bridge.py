class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_x, first_y = -1, -1
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    first_x, first_y = x, y
                    break

        queue = deque([(first_x, first_y)])
        first_island_queue = deque([(first_x, first_y, 0)])
        grid[first_x][first_y] = 2
        while(queue):
            x, y = queue.popleft()
            for d_x, d_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                n_x, n_y = x + d_x, y + d_y
                if (0 <= n_x < n) and (0 <= n_y < n) and (grid[n_x][n_y] == 1):
                    queue.append((n_x, n_y))
                    first_island_queue.append((n_x, n_y, 0))
                    grid[n_x][n_y] = 2

        while(first_island_queue):
            x, y, d = first_island_queue.popleft()
            for d_x, d_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                n_x, n_y = x + d_x, y + d_y
                if (0 <= n_x < n) and (0 <= n_y < n):
                    if grid[n_x][n_y] == 1:
                        return d
                    elif grid[n_x][n_y] == 0:
                        grid[n_x][n_y] = -1
                        first_island_queue.append((n_x, n_y, d + 1))