class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits:
            string += str(i)
        string = str(int(string)+1)
        ans = []
        for char in string:
            ans.append(int(char))
        return ans