class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        gridx=[]
        gridy=[]
        for iterator in range(len(grid[0])):
            p=0
            for iterator1 in range(len(grid)):
                if grid[iterator1][iterator]==1:
                    p+=1
            gridx.append(p)
        
        for iterator in range(len(grid)):
            gridy.append(sum(grid[iterator]))
        a=len(grid)
        b=len(grid[0])
        grid=[]
        for iterator in range(a):
            z=[]
            for iterator1 in range(b):
                z.append(gridx[iterator1]+gridy[iterator]-a+gridx[iterator1]-b+gridy[iterator])
            grid.append(z)
        return grid