class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split(" ")
        left,right = 0,len(string)-1
        print(string)
        
        while left < right:
            if string[left] == "":
                left += 1
            if string[right] == "":
                right -= 1
            string[left],string[right] = string[right],string[left]
            right -= 1
            left += 1
        ans = ''
        for i in string:
            if i != '':
                ans += (i + ' ')
        return ans[:-1]