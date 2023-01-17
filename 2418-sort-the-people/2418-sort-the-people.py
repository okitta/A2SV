class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for left in range(len(names)):
            minimum = heights[left]
            min_index = left
            for right in range(left+1,len(names)):
                if minimum < heights[right]:
                    min_index = right
                    minimum = heights[right]
            names[min_index],names[left] = names[left],names[min_index]
            heights[min_index],heights[left] = heights[left],heights[min_index]
        return names
        