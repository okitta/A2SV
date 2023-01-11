class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right_pointer = len(s)-1
        left_pointer = 0 
        while left_pointer < right_pointer:
            s[left_pointer],s[right_pointer] = s[right_pointer],s[left_pointer]
            left_pointer+=1
            right_pointer-=1
        return s
        