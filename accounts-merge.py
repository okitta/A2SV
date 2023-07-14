class UnionFind:
        def __init__(self,n):
            self.parent = [i for i in range(n)]
            self.rank = [1]*n
        
        def find(self,var):
            while var != self.parent[var]:
                self.parent[var] = self.parent[self.parent[var]]
                var = self.parent[var]
            return var
        
        def union(self,var1,var2):
            par1,par2 = self.find(var1),self.find(var2)

            if par1 == par2:
                return False

            if self.rank[par1] > self.rank[par2]:
                self.parent[par2] = par1
                self.rank[par1] += self.rank[par2]
            else:
                self.parent[par1] = par2
                self.rank[par2] += self.rank[par1]
            
            return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} 

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e) 

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res