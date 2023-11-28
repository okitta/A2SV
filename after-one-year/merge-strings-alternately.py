class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left,right = 0,0
        ans = ""
        while left < len(word1) and right < len(word2):
            if left <= right:
                ans += word1[left]
                left += 1
            else:
                ans += word2[right]
                right += 1
        if left < len(word1):
            ans += word1[left:]
        elif right < len(word2):
            ans += word2[right:]
        
        return ans