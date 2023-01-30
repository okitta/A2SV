class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        arr_word1 = list(word1) 
        arr_word2 = list(word2)
        string = ''
        while arr_word1 and arr_word2:
            string += arr_word1.pop(0) if arr_word1 > arr_word2 else arr_word2.pop(0)
        return string + ''.join(arr_word1) + ''.join(arr_word2)
        