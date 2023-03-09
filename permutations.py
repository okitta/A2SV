class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        size = len(nums)

        def backtrack(cur):
            if len(cur) == size:
                ans.append(cur[::])
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()
                    visited.remove(num)
        
        backtrack([])
        return ans