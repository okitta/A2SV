class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(nums)
        left = 0
        right = len(arr)-1

        while left < right:
            if arr[left] + arr[right] > target:
                right -= 1
            elif arr[left] + arr[right] < target:
                left += 1
            else:
                break
        ans = []

        for i in range(len(nums)):
            if nums[i] == arr[left] or nums[i] == arr[right]:
                ans.append(i)

        return ans[:2]