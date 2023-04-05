class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visit = 0
        neg = 0
        for num in nums:
            if num < 0:
                neg += 1
            for i in range(num.bit_length()):
                if (visit//10**i) % 10 == 9:
                    visit -= 9*(10**i)
                visit += int(bin(num)[-(i+1)]) * (10 ** i)
        ans = 0

        for num in str(visit):
            if int(num)%3 == 1:
                ans <<= 1
                ans |= 1
            else:
                ans <<= 1
        if neg % 3 == 0:
            return ans
        return -ans