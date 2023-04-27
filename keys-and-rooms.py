class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        check = 0
        def bfs():
            nonlocal check
            visited = set([0])
            queue = deque([0])

            while queue:
                row = queue.popleft()

                for keys in rooms[row]:
                    if keys not in visited:
                        visited.add(keys)
                        queue.append(keys)
            check = len(visited)
        bfs()
        if check == len(rooms):
            return True
        return False