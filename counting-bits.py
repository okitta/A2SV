class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            counter = 0
            while i != 0:
                if i & 1 == 1:
                    counter += 1
                i >>= 1
            ans.append(counter)
        return ans