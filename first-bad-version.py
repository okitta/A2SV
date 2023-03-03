# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 1,n
        min_val = n
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid - 1
                min_val = mid
            else:
                left = mid + 1
        return min_val