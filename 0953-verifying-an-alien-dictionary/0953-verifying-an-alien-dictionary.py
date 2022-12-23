class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dictionary = {l:i for i,l in enumerate(order)}
        for w1 , w2 in zip(words, words[1:]):
            for char1, char2 in zip(w1,w2):
                if char1 != char2:
                    if order_dictionary[char1] > order_dictionary[char2]:return False
                    break
            if w1.startswith(w2) and w1 != w2:
                return False
        return True
                    
        