from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        answer_list = defaultdict(list)
        final_answer = []
        for items in paths:
            items = items.split(' ') # spliting given array by space
            path = items.pop(0) # the first item of the splited array is the directory
            for item in items:
                bracket_index = item.index('(') # finding the index where the contents are found
                answer_list[item[bracket_index:]].append(path+'/'+item[:bracket_index]) #slicing the string and uploading in as a key while appending its path to the list
        return [iterator for iterator in answer_list.values() if len(iterator)>1] #list comprehsion for returning a 2d array