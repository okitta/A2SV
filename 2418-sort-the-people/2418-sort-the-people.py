class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for left in range(len(names)-1):
        #     for right in range(1,len(names)):
        #         if heights[left] < heights[right]:
        #             names[left],names[right] = names[right],names[left]
        # return names
        for item in range(len(heights)):
            left_pointer = 0
            right_pointer = 1
            while right_pointer < len(heights):
                if heights[left_pointer] < heights[right_pointer]:
                    names[left_pointer],names[right_pointer] = names[right_pointer],names[left_pointer]
                    heights[left_pointer],heights[right_pointer] = heights[right_pointer],heights[left_pointer]
                right_pointer +=1
                left_pointer +=1
            
        return names 
        