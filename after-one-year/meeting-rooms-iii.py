class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n
        ending_time = []
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)

        meetings.sort()

        for start,end in meetings:
            while ending_time and start >= ending_time[0][0]:
                time,room_id = heapq.heappop(ending_time)
                heapq.heappush(free_rooms,room_id)

            delay = 0

            if free_rooms:
                room_id = heapq.heappop(free_rooms)
            else:
                delay = ending_time[0][0] - start
                time,room_id = heapq.heappop(ending_time)

            heapq.heappush(ending_time,[end+delay,room_id])
            count[room_id] += 1
        return count.index(max(count)) 