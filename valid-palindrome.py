class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if len(s) == 0:
        #     return True
        string = ''.join(letter for letter in s if letter.isalnum())
        string = string.lower()
        left = 0
        right = len(string)-1
        while left <= right:
            if string[left] != string[right]:
                return False
            right -= 1
            left += 1
        return True