class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        ans = 0
        for c1,c2 in costs:
            diff.append([c2-c1,c1,c2])
        diff.sort()
        for i in range(len(costs)):
            if i < len(diff)//2:
                ans += diff[i][2]
            else:
                ans += diff[i][1]
        
        return ans