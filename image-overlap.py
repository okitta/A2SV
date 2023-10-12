class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        size = len(img1)
        inc = 2*(size-1)
        cSize = size + inc
        box = [[0 for i in range(cSize)] for i in range(cSize)]

        for i in range(size):
            for j in range(size):
                box[i+size-1][j+size-1] = img1[i][j]

        max_val = 0

        for i in range(cSize - (size -1)):
            for j in range(cSize - (size -1)):
                count = 0
                for row in range(size):
                    for col in range(size):
                        if img2[row][col] and box[row+i][col+j]:
                            count += 1
                max_val = max(max_val,count)

        return max_val