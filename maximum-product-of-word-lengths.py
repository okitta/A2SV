class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_mask = []
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            words_mask.append(mask)
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (words_mask[i] & words_mask[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res