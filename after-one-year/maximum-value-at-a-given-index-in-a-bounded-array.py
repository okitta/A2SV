class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(num,index,size):
            left = max(num-index,0)
            res = (num + left) * (num - left + 1) // 2
            right = max(num - ((size-1) - index),0)
            res += (num + right) * (num - right + 1) // 2
            return res - num
        
        maxSum -= n
        left,right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid,index,n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1