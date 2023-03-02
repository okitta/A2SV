class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        while tickets[k] > 0:
            for idx in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if tickets[idx] > 0:
                    tickets[idx] -= 1
                    counter += 1
            
        return counter