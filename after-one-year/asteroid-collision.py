class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        positive_stack,negative_stack = [],[]
        for asteroid in asteroids:
            while positive_stack and asteroid < 0 and positive_stack[-1] > 0:
                if abs(asteroid) > positive_stack[-1]:
                    positive_stack.pop()
                elif abs(asteroid) == positive_stack[-1]:
                    positive_stack.pop()
                    break
                else:
                    break 
            else:
                positive_stack.append(asteroid)
        
        return positive_stack