class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        def GCD(a,b):
            if a < b: return GCD(b,a)
            if a % b == 0: return b
            if b == 0: return a
            return GCD(b,a%b)
        def solve(nums):
            if len(nums) == 1:
                return nums[0]

            div = GCD(nums[0], nums[1])

            if len(nums) == 2:
                return div

            for i in range(1, len(nums) - 1):
                div = gcd(div, nums[i + 1])
                if div == 1:
                    return div
            return div

        hcf = solve(list(counter.values()))

        if hcf > 1: return True
        else: return False