class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        glomax = 0
        rows, cols = len(grid), len(grid[0])

        # bfs algorithm that returns an area
        def bfs(r, c):
            total = 0

            # initialize a queue
            q = collections.deque()
            q.append((r, c))
            # process queue
            while q:
                # collect from queue, mark as visited (possibly redundant), add one to total
                cr, cc = q.popleft()
                total += 1
                grid[cr][cc] = 0

                # process neighbors
                for neighbor in directions:
                    dr, dc = cr + neighbor[0], cc + neighbor[1]
                    # if valid neighbor
                    if dr >= 0 and dr < rows and dc >= 0 and dc < cols and grid[dr][dc] == 1:
                        q.append((dr, dc))
                        grid[dr][dc] = 0
                        # mark as visited
                        # add to queue

            print(total)
            return total

        # iteration w/ "1" as the insertion point
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total = bfs(r, c)
                    glomax = max(glomax, total)

        return glomax