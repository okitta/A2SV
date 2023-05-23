class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ranks = {}
        rep = {}
        for point in points:
            rep[tuple(point)] = tuple(point)
            ranks[tuple(point)] = 1

        def find(x):
            if rep[x] == x:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def connect(x,y):
            px = find(x)
            py = find(y)

            if px != py:
                if ranks[px] > ranks[py]:
                    rep[py] = px
                    ranks[py] += ranks[px]
                else:
                    rep[px] = py
                    ranks[px] += ranks[py]
        edges = []
        for i in range(len(points)):
            for j in range(i,len(points)):
                weight = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append((tuple(points[i]),tuple(points[j]),weight))
        edges.sort(key = lambda s:s[2])

        touched = 0
        mst = 0
        for edge in edges:
            u,v,w = edge

            if find(u) != find(v):
                connect(u,v)
                mst += w
                touched += 1
            
            if touched == len(points)-1:
                break
        return mst





# def solve():
#     n, m = get_ints()
#     mst = 0
#     parent = [i for i in range(n)]
#     size = [1]*n
    

#     def find(member):
#         path = []
#         while member != parent[member]:
#             path.append(member)
#             member = parent[member]
        
#         for i in range(len(path)):
#             parent[path[i]] = member
            
#         return member
    
#     def union(x,y):
#         xpar = find(x)
#         ypar = find(y)

#         if xpar != ypar:
#             if size[xpar] > size[ypar]:
#                 parent[ypar] = xpar
#                 size[xpar] += size[ypar]
#             else:
#                 parent[xpar] = ypar
#                 size[ypar] += size[xpar]
    
#     nums = get_list()
#     values = []
    
#     for i in range(n):
#         values.append((nums[i], i))
        
#     values.sort()
    
#     edges = []
#     for i in range(1, n):
#         edges.append((values[0][1], values[i][1], values[0][0] + values[i][0]))

#     for _ in range(m):
#         u, v, w = get_ints()
#         edges.append((u-1, v-1, w))
    
#     edges.sort(key=lambda x: x[2])

#     touched = 0
#     for edge in edges:
#         u,v,w = edge

#         if find(u) != find(v):
#             union(u,v)
#             mst += w
#             touched += 1
        
#         if touched == n-1:
#             break
#     return mst