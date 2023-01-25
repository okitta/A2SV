class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square = int(c**0.5)
        largest = square
        lowest = 0
        while lowest <= largest:
            if lowest**2 + largest**2 == c:
                return True
            elif lowest**2 + largest**2 > c:
                largest -= 1
            else:
                lowest += 1
        return False
        