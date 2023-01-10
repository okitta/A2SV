class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = defaultdict(int)
        result = 0
        for word in words:
            key = ' '.join(sorted(set(word)))
            result += count[key]
            count[key]+=1
        return result