class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num not in visited:
                visited.add(num)
                nums.append(num)
        left,right = 0,len(nums) - len(visited)
        while right < len(nums):
            nums[left],nums[right] = nums[right],nums[left]
            right += 1
            left += 1
        return len(visited)
            
        