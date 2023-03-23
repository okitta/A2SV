class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        size = len(nums)
        if size < 3:
            return False
        min_stack = [0]*size
        stack = []
        min_stack[0] = nums[0]
        for idx in range(1,size):
            min_stack[idx] = min(min_stack[idx-1],nums[idx])
        
        for index in range(size-1,-1,-1):
            if nums[index] <= min_stack[index]:
                continue
            while stack and stack[-1] <= min_stack[index]:
                stack.pop()
            if stack and stack[-1] < nums[index]:
                return True
            stack.append(nums[index])
        return False