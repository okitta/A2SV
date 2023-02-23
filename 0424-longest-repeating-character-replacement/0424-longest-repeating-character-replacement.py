class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1
        for index in set(s):
            prefix = [0]
            left = 0
            right = 1
            for item in s:
                prefix.append(prefix[-1])
                if item != index:
                    prefix[-1] += 1
            
            while right <= len(s):
                if prefix[right] - prefix[left] <= k:
                    ans = max(ans,right-left)
                    right +=1
                    
                else:
                    left += 1
        return ans