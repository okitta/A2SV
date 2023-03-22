class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        upper_right, lower_left, ans = sum(grid[0]), 0, math.inf
        for upper, lower in zip(grid[0], grid[1]):
            upper_right -= upper
            ans = min(ans, max(upper_right, lower_left))
            lower_left += lower
        return ans