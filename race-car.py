class Solution:
    def racecar(self, target: int) -> int:
        queue = [(0, 1)]
        position = 0
        
        while queue:
            num = len(queue)
            for i in range(num):
                pos, speed = queue.pop(0)
                if pos == target:
                    return position
                queue.append((pos+speed, speed*2))
                rev_speed = -1 if speed > 0 else 1
                if (pos+speed) < target and speed < 0 or (pos+speed) > target and speed > 0:
                    queue.append((pos, rev_speed))
            position += 1