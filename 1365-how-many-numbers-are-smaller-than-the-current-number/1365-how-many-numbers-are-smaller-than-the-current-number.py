class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums)
        for item in range(size):
            counter = 0
            if item == 0:
                for index in range(1,size):
                    if nums[index] < nums[item]:
                        counter += 1
                ans.append(counter)
            elif item == size-1:
                for value in nums[:item]:
                    if nums[item] > value:
                        counter += 1
                ans.append(counter)
            else:
                for value in nums[:item]:
                    if nums[item] > value:
                        counter += 1
                for value in nums[item+1:]:
                    if nums[item] > value:
                        counter += 1
                ans.append(counter)
        return ans
                        
        