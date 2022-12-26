class Solution:
    def interpret(self, command: str) -> str:
        answer = ""
        for i in range(len(command)):
            if command[i] ==')':
                if command[i-1] =='(':
                    answer+='o'
            elif command[i] != '(':
                answer+=command[i]         
        return answer
                    