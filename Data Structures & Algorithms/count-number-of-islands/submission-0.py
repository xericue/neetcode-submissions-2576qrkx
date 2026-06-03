class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        total = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        
        def dfs(i, j):
            q = []
            visited.add((i, j))
            q.append((i, j)) # process the first, current cell when you encounter one... duh
            
            while q:
                r, c = q.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if ((nr, nc) in visited or nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    # if grid[nr][nc] == "1":
                    dfs(nr, nc)
                    visited.add((nr, nc))
                
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    total += 1
                
        return total