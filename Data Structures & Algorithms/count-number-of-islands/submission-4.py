class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # initialization
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0
        # visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        stk = []

        # core logic
        # traversal algorithm: turn all 1s into 0s
        def dfs(r, c):
            grid[r][c] = "0"
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == "1":
                    dfs(nr, nc)

        # accumulation of values
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        # return

        return islands