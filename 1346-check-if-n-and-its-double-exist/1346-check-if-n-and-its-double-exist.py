class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dictionary = {}
        for items in arr:
            if dictionary.get(items*2,0) or dictionary.get(items/2,0):
                return True
            dictionary[items] = 1
        return False
        