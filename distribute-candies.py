class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        given = set(candyType)
        size = len(candyType)
        return len(given) if len(given) <= size//2 else size//2