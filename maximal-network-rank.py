class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)

        for city1,city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)
        
        ans = 0

        for city1,city2 in itertools.combinations(graph.keys(),2):
            has_connection = 1 if city1 in graph[city2] else 0
            city1_connection = len(graph[city1])
            city2_connection = len(graph[city2])
            ans = max(ans,city1_connection + city2_connection - has_connection)
        return ans