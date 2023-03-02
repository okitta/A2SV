class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.left = 0
        self.right = len(s) - 1
        def helperfun(s):
            if self.left >= self.right:
                return s
            print(s[self.left],s[self.right])
            s[self.left],s[self.right] = s[self.right],s[self.left]
            self.right -= 1
            self.left += 1
            return helperfun(s)
        
        helperfun(s)