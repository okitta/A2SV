class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [char for char in s.split(' ')]
        ans = ''
        for i in arr:
            ans += i[::-1]
            ans += ' '
        return ans[:-1]