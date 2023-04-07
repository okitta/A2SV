class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)
        for src,des in edges:
            graph[src].append(des)
            graph[des].append(src)

        def dfs(vertex):
            if vertex == destination:
                return True
            visited.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False
        return dfs(source)