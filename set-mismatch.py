class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        ans = []
        for idx in range(1,len(nums)+1):
            if d[idx] > 1:
                ans.append(idx)
        for idx in range(1,len(nums)+1):
            if d[idx] == 0:
                ans.append(idx)
        return ans