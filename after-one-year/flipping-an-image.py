class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for i in range(len(image))] for i in range(len(image[0]))]
        for row in image:
            row.reverse()
        for row in range(len(image)):
            for col in range(len(image[0])):
                if image[row][col] == 0:
                    matrix[row][col] = 1
                else:
                    matrix[row][col] = 0
        return matrix