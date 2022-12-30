class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left_pointer = 0
        right_pointer = len(nums)-1
        while left_pointer < right_pointer:
            # print(nums)
            if nums[right_pointer] % 2 == 0:
                if nums[left_pointer] % 2 != 0:
                    nums[left_pointer],nums[right_pointer] = nums[right_pointer],nums[left_pointer]
                    # print(nums)
                    left_pointer +=1
                    right_pointer -=1
                else:
                    left_pointer +=1
            else:
                if nums[left_pointer] % 2 == 0:
                    right_pointer -=1
                    left_pointer +=1
                else:
                    right_pointer -=1
        return nums
                    
                
        