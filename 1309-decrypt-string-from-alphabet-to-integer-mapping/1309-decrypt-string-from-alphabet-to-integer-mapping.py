class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new=""
        string_length = len(s)
        iterator = string_length - 1
        while iterator>=0:
            if s[iterator] == '#':
                new = new + alphabet[int(s[iterator-2:iterator])-1]
                iterator-=3
            else:
                new = new + alphabet[int(s[iterator])-1]
                iterator -=1
        return new[::-1]
        