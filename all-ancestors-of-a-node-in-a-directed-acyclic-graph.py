class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # ans = [set() for i in range(n)]
        ans = [[] for i in range(n)]
        graph = defaultdict(list)
        indegree = defaultdict(int)
        # visited = [False] * n
        for start,to in edges:
            graph[start].append(to)
            indegree[to] += 1
        queue = deque()
        for idx in range(n):
            if indegree[idx] == 0:
                queue.append(idx)
        # print(queue)
        while queue:
            val = queue.popleft()
            # print(val)
            for neigh in graph[val]:
                # print(ans[neigh])
                ans[neigh].extend(ans[val])
                ans[neigh].append(val)
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    ans[neigh] = list(set(ans[neigh]))
                    ans[neigh].sort()
                    queue.append(neigh)
            # print(ans)
        return ans
            
        

        # def dfs(vertex,graph,ans):
        #     stack = [(vertex,[vertex])]
        #     while stack:
        #         node,path = stack.pop()
        #         ans[node].update(path)
        #         ans[node].discard(node)
        #         for neigh in graph[node]:
        #             stack.append((neigh,path+[neigh]))
                

        # for i in range(n):
        #     dfs(i,graph,ans)
        #     ans[i].discard(i)
        
        # return ans