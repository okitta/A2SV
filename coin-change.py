class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = defaultdict(int)
        # available = set(coins)
        # coins.sort(reverse=True)
        # for i in coins:
        #     if amount%i in available:
        #         memo[i] = amount%i
        #     elif amount%i == 0:
        #         memo[i] = i
        # ans = float("inf")
        # for key,values in memo.items():
        #     ans = min(ans,amount//key+values)
        # total = 0
        # counter = 0
        # for i in coins:
        #     while total+i <= amount:
        #         print(total,i)
        #         total += i
        #         counter += 1
        #     if total == amount:
        #         break
        # if ans == float("inf"):
        #     return -1
        # return min(ans,counter)
        memo = {}
        def dp(target):
            if target == 0:
                return 1
            min_val = inf
            if target in memo:
                return memo[target]
            for coin in coins:
                if target-coin >= 0:
                    min_val = min (min_val,dp(target-coin))
            min_val += 1
            memo[target] = min_val
            return min_val
        num = dp(amount)
        return -1 if num == inf  else num-1