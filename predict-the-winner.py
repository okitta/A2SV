class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def maxscore(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i>j:
                return 0
            #
            sA = nums[i] + min( maxscore(i+1,j-1), maxscore(i+2,j  ) )
            sB = nums[j] + min( maxscore(i  ,j-2), maxscore(i+1,j-1) )
            score = max(sA,sB)
            memo[i,j] = score
            return score
        p1 = maxscore(0,len(nums)-1)
        return p1>=(sum(nums)-p1)