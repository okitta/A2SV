class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = 0
        size = len(nums)

        def backtrack(cur):
            nonlocal visited
            if len(cur) == size:
                ans.append(cur[::])
                return
            for idx in range(len(nums)):
                if visited & (1 << idx) == 0:
                    visited |= (1 << idx)
                    cur.append(nums[idx])
                    backtrack(cur)
                    cur.pop()
                    visited &= ~(1 << idx)
        
        backtrack([])
        return ans