class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pointer1 = pointer2 = 0
        while pointer1 < len(haystack) and pointer2 < len(needle):
            if pointer2 == len(needle):
                return pointer1 - len(needle)
            if haystack[pointer1] == needle[pointer2]:
                pointer2 += 1
            else:
                pointer1 = pointer1- pointer2
                pointer2 = 0
            pointer1 += 1
        if pointer2 == len(needle):
            return pointer1 - len(needle)
        return -1