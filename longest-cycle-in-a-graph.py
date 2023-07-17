class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        maxlen = 0
        def dfs(idx,depth, visited:set,cycledetec:dict):
            nonlocal maxlen
            visited.add(idx)
            cycledetec[idx] = depth 
            if edges[idx] == -1:
                return

            if edges[idx] not in visited:
                dfs(edges[idx], depth + 1, visited, cycledetec)

            elif edges[idx] in cycledetec:
                lenn = (depth - cycledetec[edges[idx]]) + 1
                maxlen = max(lenn, maxlen)
            cycledetec.pop(idx)

        for i in range(len(edges)):
            if i not in visited:
                dic = collections.defaultdict(int)
                dfs(i, 0, visited, dic)

        return maxlen if maxlen != 0 else -1