class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        idx_dict = {}
        for idx in range(len(s)):
            if s[idx] == '[':
                stack.append(idx)
            elif s[idx] == ']':
                idx_dict[stack.pop()] = idx
        
        def helperfun(left,right):
            res = []
            count = 0
            while left <= right:
                cur = s[left]
                if cur.isdigit():
                    count = count*10 + int(cur)
                elif cur == "[":
                    res.append(helperfun(left+1,idx_dict[left]-1)*count)
                    count = 0
                    left = idx_dict[left]
                else:
                    res.append(cur)
                left += 1
            return "".join(res)
        return helperfun(0,len(s)-1)