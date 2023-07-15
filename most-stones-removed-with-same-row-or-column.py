class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return

            if size[rx] <= size[ry]:
                parent[rx] = ry
                size[ry] += size[rx]
            else:
                parent[ry] = rx
                size[rx] += size[ry]
        
        def num_components():
            x = set()
            for i in range(n):
                x.add(find(i))
            return len(x)
        
        xs = {}
        ys = {}
        for i, (x, y) in enumerate(stones):
            if x in xs:
                union(i, xs[x])
            if y in ys:
                union(i, ys[y])
            xs[x] = i
            ys[y] = i
        
        return n - num_components()