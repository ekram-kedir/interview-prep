class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        queue = deque()
        queue.extend(rooms[0])
        while queue:
            
            length = len(queue)

            for ele in range(length):
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    queue.extend(rooms[node])    

        if len(visited) != len(rooms):
                return False
        return True
            