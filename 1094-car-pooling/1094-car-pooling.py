class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1001
        for trip in trips:
            numPass,start,end = trip
            arr[start] += numPass
            arr[end] -= numPass
        currPass = 0
        for item in arr:
            currPass += item
            if currPass > capacity:
                return False
        return True
        
#         trips.sort(key = lambda trip:trip[1])
#         minHeap = []
#         currPassenger = 0
        
#         for trip in trips:
#             numPassenger ,start, end = trip
            
#             while minHeap and minHeap[0][0] <= start:
#                 currPassenger -= minHeap[0][1]
#                 heapq.heappop(minHeap)
#             currPassenger += numPassenger
#             if currPassenger > capacity:
#                 return False
#             heapq.heappush(minHeap,[end,numPassenger])
#         return True