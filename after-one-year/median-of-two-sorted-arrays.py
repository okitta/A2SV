class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        heap = []
        for i in nums1:
            heappush(heap,i)
        for i in nums2:
            heappush(heap,i)
        arr = []
        for i in range(len(nums1)+len(nums2)):
            arr.append(heappop(heap))
        # print(arr)
        if len(arr)%2 != 0:
            return arr[len(arr)//2]
        else:
            # print(arr[len(arr)//2],arr[(len(arr)//2)-1])
            return (arr[len(arr)//2] + arr[(len(arr)//2)-1])/2