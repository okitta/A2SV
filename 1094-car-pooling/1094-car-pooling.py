class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda trip:trip[1])
        minHeap = []
        currPassenger = 0
        
        for trip in trips:
            numPassenger ,start, end = trip
            
            while minHeap and minHeap[0][0] <= start:
                currPassenger -= minHeap[0][1]
                heapq.heappop(minHeap)
            currPassenger += numPassenger
            if currPassenger > capacity:
                return False
            heapq.heappush(minHeap,[end,numPassenger])
        return True