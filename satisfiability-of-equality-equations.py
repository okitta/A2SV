class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def union(var1,var2):
            p1 = find(var1)
            p2 = find(var2)
            if p1 == p2:
                return
            parent[p2] = p1
        def find(var):
            if not parent.get(var):
                parent[var] = var
                return var
            if parent[var] == var:
                return var
            return find(parent[var])
        for i in equations:
            if i[1] == '=':
                p,q = i[0],i[3]
                union(p,q)
        for i in equations:
            if i[1] == '!':
                if find(i[0]) == find(i[3]):
                    return False
        return True