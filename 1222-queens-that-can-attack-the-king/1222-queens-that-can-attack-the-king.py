class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        l=[]
        for i in range(king[1],-1,-1):
            if [king[0],i] in queens:
                l.append([king[0],i])
                break

        for i in range(king[1],8,1):
            if [king[0],i] in queens:
                l.append([king[0],i])
                break

        for i in range(king[0],-1,-1):
            if [i,king[1]] in queens:
                l.append([i,king[1]])
                break
                
        for i in range(king[0],8,1):
            if [i,king[1]] in queens:
                l.append([i,king[1]])
                break
            
            

        for i in range(1,8):
            if [king[0]+i,king[1]+i] in queens:
                l.append([king[0]+i,king[1]+i])
                break
            if king[0]+i>7 or king[1]+i>7:
                break

        for i in range(1,8):
            if [king[0]-i,king[1]-i] in queens:
                l.append([king[0]-i,king[1]-i])
                break
            if king[0]-i<0 or king[1]-i<0:
                break
                
        for i in range(1,8):
            if [king[0]-i,king[1]+i] in queens:
                l.append([king[0]-i,king[1]+i])
                break
            if king[0]-i<0 or king[1]+i>7:
                break
                
        for i in range(1,8):
            if [king[0]+i,king[1]-i] in queens:
                l.append([king[0]+i,king[1]-i])  
                break 
            if king[0]+i>7 or king[1]-i<0:
                break 

        ans=[]
        for i in l:
            if i not in ans:
                ans.append(i)
        return ans