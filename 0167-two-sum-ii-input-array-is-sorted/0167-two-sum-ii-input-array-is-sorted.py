class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right_pointer = len(numbers) -1
        index = 0
        while index < right_pointer:
            if numbers[index]+numbers[right_pointer] == target:
                return [index+1,right_pointer+1]
            elif numbers[index]+numbers[right_pointer] > target:
                right_pointer -= 1
            else:
                index += 1
        