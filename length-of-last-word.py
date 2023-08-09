class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        ans = 0
        for i in arr:
            if len(i) > 0:
                ans = len(i)
        return ans