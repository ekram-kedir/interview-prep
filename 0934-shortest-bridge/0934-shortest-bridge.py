class Solution:
    def inBound(self, row, col, length):
        if row >= 0 and row < length and col >= 0 and col < length:
            return True
        return False
    
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        length = len(grid)
        dxns = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        
        def dfs(node):
            row, col = node
            if not self.inBound(row, col, length) or not grid[row][col] or node in visited:
                return

            visited.add(node)
            for dr, dc in dxns:
                new_c, new_r = col + dc, row + dr
                dfs((new_r, new_c))
        
        def bfs():
            res, q = 0, deque(visited)
            while q:
                length_q = len(q)
                for idx in range(len(q)):
                    curr_r, curr_c = q.popleft()
                    for dr, dc in dxns:
                        new_r, new_c = curr_r + dr, curr_c + dc
                        if self.inBound(new_r, new_c, length) and (new_r, new_c) not in visited:
                            if grid[new_r][new_c] == 1:
                                return res
                            q.append((new_r, new_c))
                            visited.add((new_r, new_c))
                res += 1
    
        for r in range(length):
            for c in range(length):
                if grid[r][c]:
                    dfs((r,c))
                    return bfs()
        