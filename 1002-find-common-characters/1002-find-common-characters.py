class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        total_count = [1001]*26 #initialize array to maximum word length
        initial = ord('a') #ascii value of a to find the array index for other characters
        for word in words:
            current_count = [0]*26
            # in this loop we will find the current number of characters in the given word
            for char in word:
                current_count[ord(char)-initial] +=1
            #in the loop below we will compare the occurance of character in current and total count and             #take the minimum.
            #if the character does not occur in one of the words then the minimum becomes 0
            for char in range(26):
                total_count[char] = min(total_count[char],current_count[char])
        ans = []
        # loop to append characters that exist in all given words 
        for char in range(26):
            for _ in range(total_count[char]):
                ans.append(chr(char + initial))
        return ans
        
        