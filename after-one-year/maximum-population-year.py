class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix =[]
        max_val = float("-inf")
        for log in logs:
            prefix.append([log[0],1])
            prefix.append([log[1],-1])
        prefix.sort()
        for idx in range(1,len(prefix)):
            prefix[idx][1] += prefix[idx-1][1]
            max_val = max(max_val,prefix[idx][1],prefix[idx-1][1])
        for pre in prefix:
            if pre[1] == max_val:
                return pre[0]
        
        
        