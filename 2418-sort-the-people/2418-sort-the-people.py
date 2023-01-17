class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for left in range(len(names)-1):
            next_pointer = left+1
            while heights[next_pointer] > heights[left] and next_pointer > 0:
                names[next_pointer],names[left] = names[left],names[next_pointer]
                heights[next_pointer],heights[left] = heights[left],heights[next_pointer]
                left -= 1
                next_pointer -= 1
        return names
        