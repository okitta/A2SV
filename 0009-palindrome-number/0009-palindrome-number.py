class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string= str(x)
        l=0
        r = len(string)-1
        
        for i in range(len(string)):
            while l <= r:
                if string[l] == string[r]:
                    if (r-l)>1:
                        l+= 1
                        r-=1
                    else:
                        return True
                else:
                    return False 
