class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        visited  = set()
        arr = [0]*n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        def dfs(vertex):
            count = Counter()
            label = labels[vertex]
            count[label] = 1

            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    count += dfs(neighbour)
            arr[vertex] = count[label]
            return count
        dfs(0)
        return arr