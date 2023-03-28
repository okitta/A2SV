class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def divide(left,right,arr):
            nonlocal ans
            if left == right:
                return [arr[left]]
            mid = (left + right)//2
            left_half = divide(left,mid,arr)
            right_half = divide(mid+1,right,arr)
            left_pointer = right_pointer = 0
            while left_pointer < len(left_half) and right_pointer < len(right_half):
                if (left_half[left_pointer]) > right_half[right_pointer]*2:
                    ans += len(left_half)- left_pointer
                    right_pointer += 1
                else:
                    left_pointer += 1
            return merge(left_half,right_half)
        def merge(left,right):
            arr = []
            left_pointer = right_pointer = 0
            while left_pointer < len(left) and right_pointer < len(right):
                if left[left_pointer] < right[right_pointer]:
                    arr.append(left[left_pointer])
                    left_pointer += 1
                else:
                    arr.append(right[right_pointer])
                    right_pointer += 1
            while left_pointer < len(left):
                arr.append(left[left_pointer])
                left_pointer += 1
            while right_pointer < len(right):
                arr.append(right[right_pointer])
                right_pointer += 1
            return arr
        divide(0,len(nums)-1,nums)
        return ans