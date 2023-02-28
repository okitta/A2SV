class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # self.n = n
        # self.isPowerOfFour = isPowerOfFour()
        if n == 1:
            return True
        elif n < 1:
            return False
        return self.isPowerOfFour(n/4)
        