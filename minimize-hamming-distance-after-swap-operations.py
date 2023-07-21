class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = {}
        
        def find(a):
            parent.setdefault(a,a)
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        def union(a,b):
            parent.setdefault(a,a)
            parent.setdefault(b,b)
            parent[find(a)] = parent[find(b)]
            
        for a,b in allowedSwaps:
            union(a,b)
            
        d = collections.defaultdict(dict)
        for i, val in enumerate(source):
            d[find(i)].setdefault(val, 0)
            d[find(i)][val] += 1
        
        ans = 0
        for i, val in enumerate(target):
            if val in d[find(i)]:
                d[find(i)][val] -= 1
                if not d[find(i)][val]:
                    del d[find(i)][val]
            else:
                ans += 1
            
        return ans