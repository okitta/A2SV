class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur,loc):
            if loc > len(nums):
                return
            if len(cur) <= len(nums) :
                ans.append(cur[::])
            for idx in range(loc,len(nums)):
                cur.append(nums[idx])
                backtrack(cur,idx+1)
                cur.pop()

        backtrack([],0)
        return ans