class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        # indirect = [len(ingredients[i] )for i in range(len(ingredients))]
        for val,prerequisite in prerequisites:
            graph[prerequisite].append(val)
            indegree[val] += 1
        queue = deque()
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        ans = []
        while queue:
            val = queue.popleft()
            ans.append(val)
            print(graph[val])
            for item in graph[val]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
        if len(ans) == numCourses:
            return True
        return False