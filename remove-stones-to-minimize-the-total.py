class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap =[]
        for item in piles:
            heappush(heap,-(item))
        for i in range(k):
            val = -heappop(heap)
            heappush(heap,-(val-(floor(val/2))))
        # print()
        return -sum(heap)