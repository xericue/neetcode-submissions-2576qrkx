class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        
        def bfs(node):
            q = collections.deque()
            q.append((node[0], node[1]))

            while q:
                x, y = q.popleft()
                if (x, y) in visited:
                    continue
                
                visited.add((x, y))

                for dr, dc in directions:
                    nr, nc = dr + x, dc + y

                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr, nc))


        rows = len(grid)
        cols = len(grid[0])
        total = 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited or grid[r][c] == "0":
                    continue
                bfs((r, c))
                visited.add((r, c))        
                total += 1
        
        return total
