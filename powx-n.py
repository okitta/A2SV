class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helperfun(x,n):
            if n == 1 or n == 0 or n == -1:
                return x**n
            else:
                if n%2 == 0:
                    return helperfun(x,n//2) ** 2
                else:
                    return helperfun(x,n//2) ** 2 * x

        return helperfun(x,n)