class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(i, curr_str):
            if i == len(arr):
                return len(curr_str)
            curr_max_len = len(curr_str)
            for i in range(i, len(arr)):
                if len(set(arr[i])) != len(arr[i]):
                    continue
                if len(set(curr_str + arr[i])) == len(curr_str) + len(arr[i]):
                    curr_max_len = max(curr_max_len, backtrack(i + 1, curr_str + arr[i]))
            return curr_max_len
        
        return backtrack(0, "")