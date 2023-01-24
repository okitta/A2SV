class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0
        iterator = 0
        while iterator < len(strs[0]):
            for iterator1 in range(len(strs)-1):
                if strs[iterator1][iterator] > strs[iterator1+1][iterator]:
                    counter += 1
                    break
                else:
                    pass
            iterator += 1
        return counter
                    
        