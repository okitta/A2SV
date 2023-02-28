class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        curSum=0
        prefix={0:1}
        for n in nums:
            curSum += n
            # print(curSum)
            diff = curSum -k
            # print(diff)
            res += prefix.get(diff,0)
            # print(res)
            prefix[curSum] = prefix.get(curSum,0)+1
            # print(prefix)
        return res
            
            
        