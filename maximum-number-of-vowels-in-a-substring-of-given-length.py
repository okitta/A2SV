class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = frozenset("aeiou")
        cnt = ans = sum(s[i] in vowels for i in range(k))
        for i in range(k, len(s)):
            cnt += (s[i] in vowels) - (s[i - k] in vowels)
            ans = max(cnt, ans)
        return ans