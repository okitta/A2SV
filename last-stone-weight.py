class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for item in stones:
            heappush(heap,-item)
        while len(heap) > 1:
            val1 = -(heappop(heap))
            val2 = -(heappop(heap))
            if abs(val1-val2) != 0:
                heappush(heap,-(val1-val2))
        if heap:
            return -(heap[0])
        return 0