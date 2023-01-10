# import Counter from collections
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wining = []
        losing = []
        for match in matches:
            wining.append(match[0])
            losing.append(match[1])
        no_lose = []
        one_lose = []
        counter = Counter(losing)
        for iterator in range(len(wining)):
            if counter[wining[iterator]] == 0:
                no_lose.append(wining[iterator])
            if counter[wining[iterator]] == 1:
                one_lose.append(wining[iterator])
            if counter[losing[iterator]] == 1:
                one_lose.append(losing[iterator])
        
        no_lose = list(set(no_lose))
        one_lose = list(set(one_lose))
        no_lose.sort()
        one_lose.sort()
        return [no_lose,one_lose]
            
        
            
            
        