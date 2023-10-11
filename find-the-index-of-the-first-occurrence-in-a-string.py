class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack) < len(needle):
            return -1
        window = len(needle)
        need = 0
        look = 0
        # flag = False
        for i in range(window):
            need += ((26**(window-i-1))*((ord(needle[i])-ord('a'))+1))
            look += ((26**(window-i-1))*(ord(haystack[i])-ord('a')+1))
        if look == need:
            return 0
        for i in range(window,len(haystack)):

            look -= ((ord(haystack[i-window])-ord('a')+1)*(26**(window-1)))
            look*= 26
            look += (ord(haystack[i])-ord('a')+1)
            # print(look,need,i)
            # if len(needle) == 1 and look==need:
            #     return i+1
            if look == need:
                return (i-window)+1
        return -1