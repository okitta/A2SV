from collections import Counter
class Solution:
        def findAnagrams(self, s: str, p: str) -> List[int]:
            p_size = len(p)
            s_size = len(s)
            ans = []
            dictionary = Counter(p)
            if p_size > s_size:
                return None

            window_size = p_size
            index= 0
            while window_size <= s_size:
                if Counter(s[index:window_size]) == dictionary:
                    ans.append(index)
                index += 1
                window_size += 1
            return ans
        