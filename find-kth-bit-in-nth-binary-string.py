class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helperfun(n,k):
            if n == 1:
                return "0"
            ans = helperfun(n-1,k)
            reverse = ""
            for a in ans:
                if a == "1":
                    reverse += '0'
                else:
                    reverse += '1'
            ans = ans + "1" + reverse[::-1]
            return ans
        final_result =  helperfun(n,k)
        return final_result[k-1]