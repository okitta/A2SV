class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        color = [0]*len(graph)

        def dfs(vertex):
            if color[vertex] == 2:
                return True
            if color[vertex] == 1:
                return False
            color[vertex] = 1

            for neigh in graph[vertex]:
                cur = dfs(neigh)
                if not cur:
                    return False
            result.append(vertex)
            color[vertex] = 2
            return True
        for i in range(len(graph)):
            if color[i] == 0:
                dfs(i)
        return sorted(result)