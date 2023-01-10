class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        comment = False
        sub_source = ""
        for strings in source:
            iterator = 0
            while iterator < len(strings):
                if not comment and strings[iterator:iterator+2] == '//':
                    break
                elif not comment and strings[iterator:iterator+2] == '/*':
                    comment = True
                    iterator+=1
                elif comment and strings[iterator:iterator+2] == '*/':
                    comment = False
                    iterator+=1
                elif not comment:
                    sub_source += strings[iterator]
                iterator+=1
                
            if sub_source and not comment:
                answer.append(sub_source)
                sub_source = ""
        return answer