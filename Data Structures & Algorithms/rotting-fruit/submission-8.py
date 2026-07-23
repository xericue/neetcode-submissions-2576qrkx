class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        minutes = -1
        fresh = 0

        q = collections.deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        if fresh == 0:
            return 0
            
        while q:
            minutes += 1
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                for nei in directions:
                    dr, dc = r + nei[0], c + nei[1]
                    if dr >= 0 and dr < rows and dc >= 0 and dc < cols and grid[dr][dc] == 1:
                        # about to be infected
                        fresh -= 1
                        grid[dr][dc] = 2
                        q.append((dr, dc))

        if fresh > 0:
            return -1
        return minutes