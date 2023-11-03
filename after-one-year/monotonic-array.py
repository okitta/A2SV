class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        ans = ''
        prev = nums[0]
        for idx in range(1,len(nums)):
            if idx == 1:
                if nums[idx] - prev > 0:
                    ans = 'positive'
                elif nums[idx] - prev < 0:
                    ans = 'negative'
            else:
                if (ans == 'positive' and nums[idx] - prev < 0) or (ans == 'negative' and nums[idx] - prev > 0):
                    return False
                if not ans:
                    if nums[idx] - prev > 0:
                        ans = 'positive'
                    elif nums[idx] - prev < 0:
                        ans = 'negative'
            prev = nums[idx]
        return True 


