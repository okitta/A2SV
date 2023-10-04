import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1],time[2]))
        visited = set()
        times_arr = [float("inf") for i in range(n)]
        priority_queue = [(0,k)]
        times_arr[k-1] = 0

        while priority_queue:
            current_time,current_node = heapq.heappop(priority_queue)
            
            if current_node not in visited:
                visited.add(current_node)
                for source,weight in graph[current_node]:
                    # print(source,node)
                    time = current_time + weight
                    if time < times_arr[source-1]:
                        times_arr[source-1] = time
                        heapq.heappush(priority_queue,(time,source))
        # print(times_arr)
        for i in times_arr:
            if i == float("inf"):
                return -1
        return max(times_arr)