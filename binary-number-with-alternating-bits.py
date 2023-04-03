class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # checker = []
        ans = True
        prev = n % 2
        n //= 2 
        while n >= 1:
            if n%2 == prev:
                print(n%2,n,prev)
                ans = False
            prev = n % 2
            n //= 2
        return ans
        # left,right = 0, 1
        # ans = True
        # while right < len(checker):
        #     if checker[left] == checker[right]:
        #         ans = False
        #     right += 1
        #     left += 1
        # return ans