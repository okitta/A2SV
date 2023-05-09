class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            heapify(heap)
            for col in row:
                if len(heap) == k:
                    if -col > heap[0]:
                        heappop(heap)
                        heappush(heap,-col)
                else:
                    heappush(heap,-col)
        return -heap[0]