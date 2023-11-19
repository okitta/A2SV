class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if (mid*(mid+1))//2 <= n:
                # print('left')
                left = mid+1
            else:
                # print('right')
                right = mid-1
        # print(right,left)
        return right 