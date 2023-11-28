class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack and (i == ']' or i == '}' or i == ')'):
                return False
            elif stack and (i == ']' or i == '}' or i == ')'):
                val = stack.pop()
                if (val == '(' and (i == ']' or i == '}')) or (val == '{' and (i == ']' or i == ')')) or (val == '[' and (i == ')' or i == '}')):
                    return False
            else:
                stack.append(i)
                # print(stack)
        if stack:
            # print(stack)
            return False
        return True