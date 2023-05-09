class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        group_mapping = {}
        for (u, v) in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)
                
        visited = set()
        for i in range(1, n + 1):
            if i in visited: continue
            stack = [(i, 0)]
            while stack:
                tmp_stack = []
                while stack:
                    cur_node, group = stack.pop()
                    if cur_node in group_mapping and group != group_mapping[cur_node]:
                        return False
                    if cur_node in visited: continue
                    group_mapping[cur_node] = group
                    visited.add(cur_node)
                    for child in self.graph[cur_node]:
                        tmp_stack.append((child, not group))
                stack = tmp_stack            
        return True