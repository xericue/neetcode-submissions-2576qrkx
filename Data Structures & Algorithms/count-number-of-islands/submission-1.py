class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        glototal = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        # algorithm function 
        def bfs(r, c):
            q.append((r, c))

            while q:
            # flip current to a zero
                cr, cc = q.popleft()
                grid[cr][cc] = "0"
            
            # neighbors traversal of curr/popped using directions
                for neighbor in directions:
                    dr, dc = cr + neighbor[0], cc + neighbor[1]
                    # now call bfs on them if they == 1
                    # do the whole check of validity
                    if dr >= 0 and dr < rows and dc >= 0 and dc < cols and grid[dr][dc] == "1":
                        q.append((dr, dc))

            # this wont return anything as it mutates the actual graph

        # iteration for insertion points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    glototal += 1

        return glototal

