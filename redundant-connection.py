class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {i:i for i in range(1,len(edges)+1)}
        ranks = [1] * len(edges)
        ans = [-1,-1]

        def find(x):
            if rep[x] == x:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        def connect(x,y):
            px = find(x)
            py = find(y)
            if px != py:
                if ranks[px-1] < ranks[py-1]:
                    rep[px] = py
                    ranks[py-1] += ranks[px-1]
                else:
                    rep[py] = px
                    ranks[px-1] += ranks[py-1]
            else:
                ans[0] = x
                ans[1] = y
        for source,dest in edges:
            connect(source,dest)
        return ans