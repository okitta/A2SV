class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # for items in nums:
        #     reversed_num = 0
        #     while items != 0:
        #         curr_digit = items%10
        #         reversed_num = 10* reversed_num
        #         reversed_num += curr_digit
        #         items = items//10
        #     nums.append(reversed_num)
        for items in  range(len(nums)):
            nums[items] = str(nums[items])
        for items in range(len(nums)):
            nums.append(nums[items][::-1])
        for items in range(len(nums)):
            nums[items] = int(nums[items])
        return len(set(nums))