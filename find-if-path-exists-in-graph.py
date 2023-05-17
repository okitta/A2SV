class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        reps = {i:i for i  in range(n)}

        def find(p):
            while p != reps[p]:
                p = reps[p]
            return p
        def connect(p,q):
            p = find(p)
            q = find(q)
            if p != q:
                reps[p] = q
            
        for a,b in edges:
            connect(a,b)
        return find(source) == find(destination)