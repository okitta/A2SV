class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        heap = []
        ans = []
        for i in counter:
            heappush(heap,(-counter[i],i))
        for idx in range(k):
            ans.append(heappop(heap)[1])
        return ans