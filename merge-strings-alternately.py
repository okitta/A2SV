class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        word1_length = len(word1)
        word2_length = len(word2)
        max_length = max(word1_length,word2_length)
        for iterator in range(max_length):
            if iterator < word1_length:
                answer+=word1[iterator]
            if iterator < word2_length:
                answer+=word2[iterator]
        return answer