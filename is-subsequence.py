class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer1 = pointer2 = counter = 0
        # ans = False
        while pointer1 < len(s) and pointer2 < len(t):
            if s[pointer1] == t[pointer2]:
                counter += 1
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2 += 1
        return counter == len(s)