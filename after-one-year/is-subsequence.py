class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = ""
        idx = 0
        if s == t:
            return True
        for char in t:
            if idx < len(s) and char == s[idx]:
                ans += char
                idx += 1
            if ans == s:
                return True
        return False