class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # init
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = collections.deque()
        fresh = 0
        # oranges = 0
        minutes = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        # maybe a visited set?
        visited = set()

        # logic
        # 1. get all the oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        if fresh == 0:
            return 0

        # 2. layer by layer bfs to populate values
        # make a function later
        while q:

            lq = len(q)
            for i in range(lq):
                r, c = q.popleft()

                # if (r, c) in visited:
                #     continue
                # visited.add((r, c))

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1    

            if q:
                minutes += 1    


        # return
        if fresh != 0:
            return -1
        return minutes