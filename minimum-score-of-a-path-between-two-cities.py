class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        reps = {i:i for i  in range(1,n+1)}
        ranks = [1] * n
        distance = 10**4

        def find(p):
            if reps[p] == p:
                return p
            reps[p] = find(reps[p])
            return reps[p]
        def connect(x,y):
            px = find(x)
            py = find(y)
            if ranks[px-1] < ranks[py-1]:
                reps[px] = py
                ranks[py-1] += ranks[px-1]
            else:
                reps[py] = px
                ranks[px-1] += ranks[py-1]
            
        for a,b,dist in roads:
            connect(a,b)
        for a,b,dist in roads:
            if find(a) == find(1):
                distance = min(distance,dist)
        return distance