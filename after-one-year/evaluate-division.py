class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for idx,eq in enumerate(equations):
            a,b = eq
            graph[a].append((b,values[idx]))
            graph[b].append((a,1/values[idx]))
        
        def bfs(src,trgt):
            if src not in graph or trgt not in graph:
                return -1
            q,visited = deque() , set()

            q.append([src,1])
            visited.add(src)

            while q:
                node,weight1 = q.pop()

                if node == trgt:
                    return weight1
                
                for neightbour,weight2 in graph[node]:
                    if neightbour not in visited:
                        q.append([neightbour,weight2*weight1])
                        visited.add(neightbour)
            
            return -1

        return [bfs(query[0],query[1]) for query in queries]