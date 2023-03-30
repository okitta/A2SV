class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hum = x^y
        return hum.bit_count()