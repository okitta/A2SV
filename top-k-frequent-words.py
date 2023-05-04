class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequence = Counter(words)
        heap = []
        ans = []
        for item in frequence:
            heappush(heap,(-(frequence[item]),item))
        for i in range(k):
            ans.append(heappop(heap)[1])
        return ans