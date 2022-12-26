class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        check_list = []
        for iterator in range(len(nums)):
            if nums[iterator] == val:
                check_list.append(iterator)
        check_list.reverse()
        for iterator in check_list:
            nums.pop(iterator)
                
        return (len(nums))