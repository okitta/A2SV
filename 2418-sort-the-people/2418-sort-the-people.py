class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for left in range(len(names)):
            max_index = left
            for right in range(left+1,len(names)):
                if heights[max_index] < heights[right]:
                    max_index = right
                    heights[max_index] = heights[right]
            names[max_index],names[left] = names[left],names[max_index]
            heights[max_index],heights[left] = heights[left],heights[max_index]
        return names
        