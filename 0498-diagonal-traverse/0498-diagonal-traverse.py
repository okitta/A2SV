class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_length = len(mat)
        column_length = len(mat[0])
        diagonalDict = defaultdict(list)
        for row in range(row_length):
            for column in range(column_length):
                diagonalDict[row+column].append(mat[row][column])
        ans = []
        for item, value in enumerate(diagonalDict.values()):
            if item % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
        return ans