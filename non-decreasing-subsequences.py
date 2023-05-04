class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # size = len(nums)

        # def backtrack(start,cur):
        #     # nonlocal visited
        #     if len(cur) >= 2:
        #         print(cur)
        #         ans.append(cur[::])
        #         # return
        #     visited = set()
        #     for idx in range(start,len(nums)):
        # #         if not cur or (nums[idx] not in visited and nums[idx] <= cur[-1]):
        # #             visited.add(nums[idx])
        # #             backtrack(start+1,cur+[nums[idx]])
        #         if not cur or (nums[idx] not in visited and nums[idx] >= cur[-1]):
        #             visited.add(nums[idx])
        #             backtrack(start + 1, cur + [nums[idx]])
        
        # backtrack(0,[])
        # return ans
        ans = []
    
        def dfs(start: int, path: List[int]) -> None:
            if len(path) > 1:
                ans.append(path[:])
            
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return ans