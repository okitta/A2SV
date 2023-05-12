class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [set() for i in range(len(quiet))]
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for richer,than in richer:
            graph[richer].append(than)
            indegree[than] += 1
        # print(grap)
        queue = deque()
        for idx in range(len(quiet)):
            if indegree[idx] == 0:
                queue.append(idx)
        while queue:
            val = queue.popleft()
            for neigh in graph[val]:
                ans[neigh].update(ans[val])
                ans[neigh].add(val)
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        res = []
        for i in range(len(quiet)):
            min_val = quiet[i]
            idx = i
            for j in range(len(quiet)):
                if j in ans[i] and quiet[j] <= min_val:
                    min_val = quiet[j]
                    idx = j
            res.append(idx)
        return res