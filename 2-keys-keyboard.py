class Solution:
    def minSteps(self, n: int) -> int:
        dictionary = {}
        def helper(screen, clipboard):
            if (screen, clipboard) in dictionary: return dictionary[(screen, clipboard)]
            if screen == n: return 0
            if screen > n: return float("Inf")
            
            copy_paste = helper(screen+screen, screen) + 2
            paste = float("Inf")
            if clipboard:
                paste = helper(screen + clipboard, clipboard) + 1

            dictionary[(screen, clipboard)] = min(copy_paste, paste)    
            return dictionary[(screen, clipboard)]
        return helper(1, 0)