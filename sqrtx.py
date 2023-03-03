class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = 0,x
        sqrt = 0
        while left <= right:
            mid = (left + right) // 2
            if mid*mid > x:
                right = mid - 1
            elif mid*mid < x:
                left = mid + 1
                sqrt = max(mid,sqrt)
            else:
                return mid
        return sqrt