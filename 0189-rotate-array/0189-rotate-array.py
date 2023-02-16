class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        while k > size:
            k = k%size
        for index in range(k):
            poped = nums.pop()
            nums.insert(0,poped)