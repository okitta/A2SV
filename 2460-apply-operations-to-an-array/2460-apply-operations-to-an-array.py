class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = 1
        size = len(nums)
        while right_pointer < size:
            if nums[left_pointer] == nums[right_pointer]:
                nums[left_pointer] *= 2
                nums[right_pointer] = 0
            else:
                pass
            left_pointer +=1
            right_pointer +=1
        read = 0
        write = 0
        while read < size:
            if nums[read] != 0:
                nums[read],nums[write] = nums[write],nums[read]
                write += 1
            read+=1
        return nums