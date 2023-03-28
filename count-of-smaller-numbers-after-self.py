class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)

        for idx in range(len(nums)):
            nums[idx] = (idx,nums[idx])


        def divide(left,right,arr):
            if left == right:
                return [arr[left]]
            mid = (left + right)//2
            left_half = divide(left,mid,arr)
            right_half = divide(mid+1,right,arr)
            left_pointer = len(left_half)-1 
            right_pointer = len(right_half)-1
            while left_pointer >= 0 and right_pointer >= 0:
                if left_half[left_pointer][1] > right_half[right_pointer][1]:
                    ans[left_half[left_pointer][0]] += right_pointer+1
                    left_pointer -= 1
                else:
                    right_pointer -= 1
            return merge(left_half,right_half)


        def merge(left,right):
            arr = []
            left_pointer = right_pointer = 0
            while left_pointer < len(left) and right_pointer < len(right):
                if left[left_pointer][1] < right[right_pointer][1]:
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