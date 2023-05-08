class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_dict = defaultdict(list)

        for node,edges in enumerate(graph):
            graph_dict[node] = edges
        
        ans = []

        def dfs(cur_path,cur_node):
            if cur_node == len(graph_dict) - 1:
                ans.append(cur_path[::])
            
            for connection in graph_dict[cur_node]:
                cur_path.append(connection)
                dfs(cur_path,connection)
                cur_path.pop()
        
        dfs([0],0)
        return ans