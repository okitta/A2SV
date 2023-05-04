class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)
        self.heap = []
        for idx in range(min(k,len(self.nums))):
            heappush(self.heap,(self.nums[idx]))
        

    def add(self, val: int) -> int:
        heappush(self.heap,(val))
        if len(self.heap)>self.k:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)