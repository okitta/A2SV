class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = len(s)
        last = {s[i]: i for i in range(size)}
        index, ans = 0, []
        while index < size:
            end, j = last[s[index]], index + 1
            while j < end:
                if last[s[j]] > end:
                    end = last[s[j]]
                j += 1
           
            ans.append(end - index + 1)
            index = end + 1
            
        return ans
                
        
        