class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        size = len(nums)
        nums.sort()
        left = 0
        right = size-1
        counter = 0
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                counter += 1
                left += 1
                right -= 1
        return counter