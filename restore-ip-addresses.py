class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        k = 0
        self.backtrack(s,ans,k,'')
        return ans
    


    def backtrack(self, s, ans,k, temp=''):
        if k==4 and len(s)==0:
            ans.append(temp[:-1])
            return
        if k==4 or len(s)==0:
            return
        
        for i in range(3):
            if k>4 or i+1>len(s):
                break
            
            if int(s[:i+1])>255:
                continue
            if i != 0 and s[0]=='0':
                continue
                    
            self.backtrack(s[i+1:], ans, k+1, temp+s[:i+1]+'.')