class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        array = [0]*(len(s)+1)
        ans = ''
        for item in shifts:
            if item[2] == 1:
                array[item[0]] += 1
                array[item[1]+1] -= 1
                    
            else:
                array[item[0]] -= 1
                array[item[1]+1] += 1
                
        for num in range(1,len(array)):
            array[num] = array[num-1] + array[num]
        
        new_arr = []
        for index in range(len(array)-1):
            new_arr.append((((ord(s[index])-ord('a'))+array[index])%26) + ord('a'))
            ans += chr(new_arr[index])
        
        # for val in new_arr:
        #     ans += chr(val)
        
        return ans