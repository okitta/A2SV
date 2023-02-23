class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        right = len(s1)
        cur = list(s2[:right])
        if Counter(cur) == counter_s1:
            return True
        for index in range(right,len(s2)):
            cur.pop(0)
            cur.append(s2[index])
            if counter_s1 == Counter(cur):
                return True
        return False
