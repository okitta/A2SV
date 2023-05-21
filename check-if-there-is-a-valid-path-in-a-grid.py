class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        n, m = len(grid), len(grid[0])
        p, rank = [[(i, j) for j in range(m)] for i in range(n)], [[1 for _ in range(m)] for _ in range(n)]

        def get(i, j):
            while p[i][j] != (i, j):
                i, j = p[i][j]
            return i, j

        def connect(i1, j1, i2, j2):
            i1, j1 = get(i1, j1)
            i2, j2 = get(i2, j2)
            if rank[i1][j1] >= rank[i2][j2]:
                p[i2][j2] = p[i1][j1]
                rank[i1][j1] += 1
            else:
                p[i1][j1] = p[i2][j2]
                rank[i2][j2] += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] in [1, 4, 6] and j+1 < m and grid[i][j+1] in [1, 3, 5]:
                    connect(i, j, i, j+1)
                if grid[i][j] in [2, 3, 4] and i+1 < n and grid[i+1][j] in [2, 5, 6]:
                    connect(i, j, i+1, j)

        return get(0, 0) == get(n-1, m-1)
        # graph = {
        #     1:[(0,-1),(0,1)],
        #     2:[(-1,0),(1,0)],
        #     3:[(1,0),(0,-1)],
        #     4:[(1,0),(0,1)],
        #     5:[(0,-1),(-1,0)],
        #     6:[(-1,0),(0,-1)],
        # }
        # reps= defaultdict(tuple)
        # ranks= [[1 for i in range(len(grid[0]))] for i in range(len(grid))]
        # # print(ranks)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         reps[(i,j)] = (i,j)
        # directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # def check(row,col):
        #     return True if row < len(grid) and row >= 0 and col < len(grid[0]) and col >=0 else False

        # def find(x,y):
        #     # if reps[(x,y)] == (x,y):
        #     #     return (x,y)
        #     # reps[(x,y)] = find(reps[(x,y)][0],reps[(x,y)][1])
        #     # return reps[(x,y)]
        #     while reps[(x,y)] != (x,y):
        #         x,y = reps[(x,y)]
        #     return (x,y)
        # def connect(row_1,col_1,row_2,col_2):
        #     for x in graph[grid[row_1][col_1]]:
        #         if (x[0],x[1]) in graph[grid[row_2][col_2]]:
        #             px = find(row_1,col_1)
        #             py = find(row_2,col_2)

        #             if ranks[px[0]][px[1]] < ranks[py[0]][py[1]]:
        #                 reps[px] = py
        #                 ranks[py[0]][py[1]] += 1
        #             else:
        #                 reps[py] = px
        #                 ranks[px[0]][px[1]] += 1
            
        # # for row in range(len(grid)):
        # #     for col in range(len(grid[0])):
        # #         for direction in directions:
        # #             if direction in graph[grid[row][col]]:
        # #                 new_row = row+direction[0]
        # #                 new_col = col+direction[1]
        # #                 if check(new_row,new_col):
        # #                     connect(row,col,new_row,new_col)
        # # print(find(0,0),find(len(grid)-1,len(grid[0])-1))
        # # if find(0,0) == find(len(grid)-1,len(grid[0])-1):
        # #     return  True
        # # return False
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] in [1, 4, 6] and j+1 < m and grid[i][j+1] in [1, 3, 5]:
        #             connect(i, j, i, j+1)
        #         if grid[i][j] in [2, 3, 4] and i+1 < n and grid[i+1][j] in [2, 5, 6]:
        #             connect(i, j, i+1, j)

        # return find(0, 0) == find(n-1, m-1)