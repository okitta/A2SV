from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for edge,weight in zip(edges,succProb):
            src,dst = edge
            graph[src].append((dst,weight))
            graph[dst].append((src,weight))
        
        def dijkstra(graph,start,end):
            distances = [float('inf') for i in range(n)]
            distances[start] = 0
            visited = set()

            heap = [(-1,start)]

            while heap:
                current_distance,current_node = heapq.heappop(heap)

                if current_node == end:
                    return -current_distance

                if current_node not in visited:
                    visited.add(current_node)

                    for neighbour,weight in graph[current_node]:
                        distance = current_distance * weight
                        if distance < distances[neighbour]:
                            distances[neighbour] = float(distance)
                            heapq.heappush(heap,(distance,neighbour))
            
            return 0
        
        return dijkstra(graph,start_node,end_node)
        # print(ans)