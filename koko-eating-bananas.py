class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        min_val = right = max(piles)
        while left <= right:
            mid = (left + right) //2
            time_count = self.findTime(piles,mid)
            if time_count <= h:
                min_val = min(min_val,mid)
                right = mid-1
            else:
                left = mid + 1
        return min_val

    def findTime(self,arr,eats):
        time = 0
        for val in arr:
            if val <= eats:
                time += 1
            else:
                time += ceil(val/eats)
        return time