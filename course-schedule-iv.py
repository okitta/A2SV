import heapq
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [False]*len(queries)
        exist = [[float("inf")]*numCourses for i in range(numCourses)]
        graph = defaultdict(list)
        for source,dest in prerequisites:
            exist[source][dest] = 1
        
        for i in range(numCourses):
            exist[i][i] = 0
        
        
        for k in range(numCourses):
            for j in range(numCourses):
                for i in range(numCourses):
                     exist[i][j] = min(exist[i][j], exist[i][k] + exist[k][j])
        for idx,query in enumerate(queries):
            if exist[query[0]][query[1]] != float("inf"):
                ans[idx] = True
            else:
                ans[idx] = False

        return ans