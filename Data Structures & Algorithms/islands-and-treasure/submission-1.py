class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])

        # cannot go to -1s
        # 0 is good
        # INF is traversable
        
        # goal: fill INFs w/ distance to nearest treasure chest
        # if not possible, make it remain INF

        # modify the grid in place
        # no need to return

        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            l = len(q)

            # need to add some </comparison so we aren't replacing
            # this is most likely why the INF exists
            for i in range(l):
                r, c = q.popleft()
                for nei in directions:
                    dr, dc = r + nei[0], c + nei[1]
                    if dr >= 0 and dc >= 0 and dr < rows and dc < cols and grid[dr][dc] > grid[r][c]:
                        grid[dr][dc] = grid[r][c] + 1
                        q.append((dr, dc))