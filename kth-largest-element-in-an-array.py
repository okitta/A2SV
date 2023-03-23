import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(array, low, high):
            pivot = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            return i + 1


        def quickSort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                if len(array) - pi < k:
                    quickSort(array, low, pi - 1)
                elif len(array) - pi > k:
                    quickSort(array, pi + 1, high)
        quickSort(nums,0,len(nums)-1)
        return nums[-k]