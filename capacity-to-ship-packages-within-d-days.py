class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        min_val = right
        while left <= right:
            mid = (left + right)//2
            weigh_count = self.find_weigh(weights,mid)
            print(mid,weigh_count)
            if weigh_count <= days:
                min_val = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_val


    def find_weigh(self,arr,capacity):
        load = capacity
        cur = 1
        for val in arr:
            if load >= val:
                load -= val
            else:
                cur += 1
                load = capacity
                load -= val
        return cur