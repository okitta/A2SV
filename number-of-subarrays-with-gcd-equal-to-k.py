class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def GCD(a, b):
            if a < b: return GCD(b, a)
            if b == 0: return a 
            if a % b == 0: return b 
            return GCD(b, a % b)

        res, prevH = 0, collections.defaultdict(int)
        if nums[0] == k: res += 1
        prevH[nums[0]] += 1

        for i in range(1, len(nums)):
            H = collections.defaultdict(int)
            prevH[nums[i]] += 1
            for prev_gcd, freq in prevH.items():
                gcd = GCD(prev_gcd, nums[i])

                if gcd == k:
                    res += freq
                H[gcd] += freq
            prevH = H 
        return res