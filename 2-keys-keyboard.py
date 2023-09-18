class Solution:
    def minSteps(self, n: int) -> int:
        dict_char_num = {}

        def dfs(num,chart):
            if (num,chart) in dict_char_num: return dict_char_num[(num,chart)]
            if num == n: return 0
            if num > n: return float("Inf")

            copy = dfs(num+num,num) + 2
            paste = float("Inf")
            if chart:
                paste = dfs(num+chart,chart) + 1
            
            dict_char_num[(num,chart)] = min(copy,paste)
            return dict_char_num[(num,chart)]
        
        return dfs(1,0)