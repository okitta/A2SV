class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = [iterator for iterator in range(1,n+1)]
        # for iterator in range(0,k*n,k):
        #     print(array)
        #     if len(array) == 1:
        #         break
        #     array.pop((iterator-1)%(len(array)))
        # return array[0]
        iterator = 0
        while len(array) > 1:
            iterator = (iterator + k -1) % len(array)
            del array[iterator]
        return array[0]