class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def helperfun(rowIndex):
            if rowIndex == 0:
                return [1]

            arr = [1]* (rowIndex+1)
            newArr = helperfun(rowIndex - 1)
            for idx in range(1,math.ceil((rowIndex+1)/2)):
                numSum = sum(newArr[idx-1:idx+1])
                arr[idx] = numSum
                arr[rowIndex-idx] = numSum
            return arr
        
        return helperfun(rowIndex)