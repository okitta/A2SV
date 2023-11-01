class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        count_set = set()
        for val in count.values():
            count_set.add(val)
        return len(count_set) == len(set(arr))