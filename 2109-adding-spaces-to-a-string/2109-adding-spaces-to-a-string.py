class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        for space in range(len(spaces)):
            if space==0:
                answer += f"{s[:spaces[space]]} "
            else:
                answer += f"{s[spaces[space-1]:spaces[space]]} "
        answer+= s[spaces[-1]:]
        return answer
        