class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        stack = []
        left = 0
        right = 1
        while arr[left] < arr[right]:
            stack.append(right)
            left += 1
            right += 1
        return stack[-1]