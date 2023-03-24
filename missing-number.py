class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_element = max(nums)
        min_element = min(nums)
        counter = [iterator for iterator in range(len(nums)+1)]
        print(counter)
        for iterator in counter:
            if iterator not in nums:
                return iterator
        return max_element+1