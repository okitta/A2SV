from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        count_dict_t = dict(Counter(sorted_t))
        count_dict_s = dict(Counter(sorted_s))
        # print(count_dict.items())
        for item in count_dict_t:
            if item not in s or count_dict_t[item] > count_dict_s[item]:
                return item
        