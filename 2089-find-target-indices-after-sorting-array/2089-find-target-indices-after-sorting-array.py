class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        l=[]
        for k in range(len(sorted_nums)):
            if sorted_nums[k] == target:
                l.append(k)
        return l