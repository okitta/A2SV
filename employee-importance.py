"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {employe.id: element for element, employe in enumerate(employees)}

        def dfs(employe_id):
            ans = employees[graph[employe_id]].importance
            for i in employees[graph[employe_id]].subordinates:
                ans += dfs(i)
            return ans
        return dfs(id)