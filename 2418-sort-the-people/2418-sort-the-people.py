class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for left in range(len(names)-1):
            max_number = left+1
            while heights[max_number] > heights[left] and max_number > 0:
                names[max_number],names[left] = names[left],names[max_number]
                heights[max_number],heights[left] = heights[left],heights[max_number]
                left -= 1
                max_number -= 1
        return names
        