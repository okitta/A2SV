class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        right+= 1
        prime = [False,False]+[True]*(right-2)
        for i in range(2,isqrt(right)+1):
                for j in range(i * i, right, i):
                    prime[j] = False
        prime = [i for i,p in enumerate(prime)      
                 if p and left<=i<=right] 
        if len(prime) < 2: return [-1,-1]
        return list(min(list(zip(prime,prime[1:])),
                    key = lambda x: x[1]-x[0]))