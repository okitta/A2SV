class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        two_power = [2**iterator for iterator in range(22)]
        dictionary = Counter(deliciousness)
        counter = 0
        for key,value in dictionary.items():
            for element in two_power:
                sub_element = element - key
                if sub_element in dictionary and sub_element == key:
                    counter += value*(value-1)//2
                elif sub_element in dictionary and sub_element != key:
                    counter += value*dictionary[sub_element]/2
        return int(counter)%(10**9 + 7)
                    