class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis = math.inf
        ans = -1
        for iterator in range(len(points)):
            if points[iterator][0] == x or points[iterator][1]==y:
                current_distance = abs(x-points[iterator][0])+abs(y-points[iterator][1])
                if current_distance < min_dis:
                    min_dis = current_distance
                    ans = iterator
        return ans