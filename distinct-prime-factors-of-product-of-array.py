class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_set = set()
        product = 1
        def prime_factor(val):
            d = 2
            while d*d <= val:
                while val % d == 0:
                    val //= d
                    prime_set.add(d)
                if d == 2:
                    d += 1
                else:
                    d += 2
            if val > 1:
                prime_set.add(val)
            
        for num in nums:
            prime_factor(num)
        return len(prime_set)