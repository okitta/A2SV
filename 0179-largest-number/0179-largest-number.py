class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        size = len(nums)
        ans = ''
        for index in range(size):
            for index2 in range(index,size):
                string1 = str(nums[index])+str(nums[index2])
                string2 = str(nums[index2])+str(nums[index])
                if int(string1) < int(string2):
                    nums[index],nums[index2] = nums[index2],nums[index]
        for item in nums:
            ans += str(item)
        check = ans.count('0')
        if check == len(ans):
            return '0'
        return ans
        
        
        