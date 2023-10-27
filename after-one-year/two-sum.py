class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for idx in range(len(nums)):
            ans.append([nums[idx],idx])
        ans.sort()
        left = 0
        right = len(nums)-1
        # res = []
        while left < right:
            if ans[left][0] + ans[right][0] == target:
                return [ans[left][1],ans[right][1]]
            elif ans[left][0] + ans[right][0] < target:
                left += 1
            else:
                right -= 1
            