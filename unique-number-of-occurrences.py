class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        visited = set()
        ans = True
        for value in counter.values():
            if value in visited:
                ans = False
                break
            visited.add(value)
        return ans