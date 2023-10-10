class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        score_age = []
        for x,y in zip(scores,ages):
            score_age.append((x,y))
        score_age.sort()
        dp = [score[0] for score in score_age]
        print(dp,"*******",score_age)
        for i in range(len(score_age)):
            mScr,mAge = score_age[i]
            for j in range(i):
                score,age = score_age[j]
                if mAge >= age:
                    dp[i] = max(dp[i],mScr+dp[j])
        return max(dp)