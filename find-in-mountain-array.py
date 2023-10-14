# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binary_inc(start,end):
            
            left = start
            right = end
            
            while left <= right:
                mid = left + (right - left) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        def binary_dec(start,end):
            
            left = start
            right = end
            
            while left <= right:
                mid = left + (right - left) // 2
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1

        left = 0
        right = mountain_arr.length() - 1
        idx = 0
        
        while left <= right:
            mid = left + (right - left )//2
            val = mountain_arr.get(mid)
            l = -float("inf") if mid == 0 else mountain_arr.get(mid-1)
            r = mountain_arr.get(mid+1)
            if val > l and val > r:
                idx = mid
                break
            elif val < r:
                left = mid + 1
            else:
                right = mid - 1
        
        left = binary_inc(0,idx)
        if left > -1:
            return left
        right = binary_dec(mid+1,mountain_arr.length()-1)
        
        return right