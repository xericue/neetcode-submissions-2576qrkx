class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        minutes -= 1
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
            
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            leng = len(q)
            for _ in range(leng):
                r, c = q.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1
                    