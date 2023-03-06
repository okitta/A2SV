class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def smallest_divisor(arr,n):
            total = 0
            for idx in range(len(arr)):
                total += ceil(arr[idx]/n)
            return total    
            

        left = 1
        right = max(nums)
        # min_val = 0
        
        while left < right:
            mid = (left+right)//2
            val = smallest_divisor(nums,mid)
            if val <= threshold:
                # min_val = right
                right = mid
            else:
                left = mid + 1
        return right