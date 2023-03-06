class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        info = []
        for i in range(len(position)):
            info.append([position[i], speed[i]])
        info.sort()
        for val in info:
            while stack and (target - val[0]) / val[1] >= (target - stack[-1][0]) / stack[-1][1]:
                stack.pop()
            stack.append(val)

            
        return len(stack)